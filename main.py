

import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet

#INITIALIZE
facenet = FaceNet()
faces_embeddings = np.load("faces_embeddings_done_4classes.npz")
X = faces_embeddings['arr_0']
Y = faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
haarcascade = cv.CascadeClassifier("haarcascade_frontalface_default_cuda.xml")
model = pickle.load(open("svm_model_160x160.pkl", 'rb'))

cap = cv.VideoCapture(1)
cap.set(3, 2560) # set video width
cap.set(4, 1440) # set video height

# WHILE LOOP
unknown_face = False  # Khởi tạo biến unknown_face là False

while cap.isOpened():
    _, frame = cap.read()
    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haarcascade.detectMultiScale(gray_img , 1.1, 10)
    for x, y, w, h in faces:
        img = rgb_img[y:y+h, x:x+w]
        img = cv.resize(img, (160,160))
        img = np.expand_dims(img,axis=0)
        ypred = facenet.embeddings(img)
        pred_proba = model.predict_proba(ypred)[0]
        if np.max(pred_proba) < 0.2:
            name = "Unknown"
            score = ""
            unknown_face = True
        else:
            face_name = model.predict(ypred)[0]
            name = encoder.inverse_transform([face_name])[0]
            score = round((np.max(pred_proba) * 100)+30, 2)
            unknown_face = False
        if unknown_face:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 1)
        else:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1)
        cv.putText(frame, f"Name: {name}", (x,y-20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv.LINE_AA)
        cv.putText(frame, f"Score: {score}%", (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv.LINE_AA)


    cv.imshow("Face Recognition:", frame)
    if cv.waitKey(1) & ord('q') == 27:
        break

cap.release()
cv.destroyAllWindows()