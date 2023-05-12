import os
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.image_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        pixmap = QtGui.QPixmap("assets/logoSPKT.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.setObjectName("image_label")

        self.image_label1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_label1.setGeometry(QtCore.QRect(1135, 0, 0, 0))
        pixmap = QtGui.QPixmap("assets/logoCLC.png")
        self.image_label1.setPixmap(pixmap)
        self.image_label1.setFixedSize(pixmap.size())
        self.image_label1.setObjectName("image_label1")

        font = QtGui.QFont()
        font.setPointSize(20)
        self.truong_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.truong_label.setGeometry(QtCore.QRect(480, 130, 0, 0))
        self.truong_label.setObjectName("truong_label")
        self.truong_label.setText("<b>TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP.HCM</b>")
        self.truong_label.setFont(font)
        self.truong_label.adjustSize()

        self.khoa_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.khoa_label.setGeometry(QtCore.QRect(550, 180, 0, 0))
        self.khoa_label.setObjectName("khoa_label")
        self.khoa_label.setText("<b>KHOA ĐÀO TẠO CHẤT LƯỢNG CAO</b>")
        self.khoa_label.setFont(font)
        self.khoa_label.adjustSize()

        self.nganh_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.nganh_label.setGeometry(QtCore.QRect(560, 230, 0, 0))
        self.nganh_label.setObjectName("nganh_label")
        self.nganh_label.setText("<b>NGÀNH CÔNG NGHỆ THÔNG TIN</b>")
        self.nganh_label.setFont(font)
        self.nganh_label.adjustSize()

        self.baocao_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.baocao_label.setGeometry(QtCore.QRect(665, 310, 0, 0))
        self.baocao_label.setObjectName("baocao_label")
        self.baocao_label.setText("<b>BÁO CÁO CUỐI KỲ</b>")
        self.baocao_label.setFont(font)
        self.baocao_label.adjustSize()

        self.mon_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.mon_label.setGeometry(QtCore.QRect(645, 350, 0, 0))
        self.mon_label.setObjectName("mon_label")
        self.mon_label.setText("<b>MÔN: XỬ LÝ ẢNH SỐ</b>")
        self.mon_label.setFont(font)
        self.mon_label.adjustSize()

        self.detai_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.detai_label.setGeometry(QtCore.QRect(310, 390, 0, 0))
        self.detai_label.setObjectName("detai_label")
        self.detai_label.setText("<b>ĐỀ TÀI: <font color='red'>NHẬN DẠNG KHUÔN MẶT BẰNG NGÔN NGỮ LẬP TRÌNH PYTHON</font></b>")
        self.detai_label.setFont(font)
        self.detai_label.adjustSize()

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 455, 80, 32))
        self.pushButton.setStyleSheet(
            "border-radius: 5px; background-color: #ccc;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("RUN")

        font.setPointSize(10)
        self.status_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(755, 490, 0, 0))
        self.status_label.setObjectName("status_label")
        self.status_label.setFont(font)

        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(740, 520, 80, 32))
        self.exitButton.setStyleSheet(
            "border-radius: 5px; background-color: #ccc;")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("EXIT")
        self.exitButton.setVisible(False)

        font.setPointSize(15)
        self.nhom_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.nhom_label.setGeometry(QtCore.QRect(110, 630, 0, 0))
        self.nhom_label.setObjectName("nhom_label")
        self.nhom_label.setText("<b>THÀNH VIÊN NHÓM 11:</b>")
        self.nhom_label.setFont(font)
        self.nhom_label.adjustSize()

        self.thanhvien_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.thanhvien_label.setGeometry(QtCore.QRect(110, 660, 0, 0))
        self.thanhvien_label.setObjectName("thanhvien_label")
        self.thanhvien_label.setText("Đoàn Thái Sơn - 21110289\n"
                                     +"Nguyễn Khánh Quy - 21110282\n"
                                     +"Nguyễn Hồng Thông Điệp - 21110166")
        self.thanhvien_label.setFont(font)
        self.thanhvien_label.adjustSize()

        self.gvhd_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.gvhd_label.setGeometry(QtCore.QRect(1100, 630, 0, 0))
        self.gvhd_label.setObjectName("gvhd_label")
        self.gvhd_label.setText("<b>GVHD: PGS.TS. Hoàng Văn Dũng</b>")
        self.gvhd_label.setFont(font)
        self.gvhd_label.adjustSize()

        self.mlhp_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.mlhp_label.setGeometry(QtCore.QRect(1100, 660, 0, 0))
        self.mlhp_label.setObjectName("mlhp_label")
        self.mlhp_label.setText("Mã lớp học phần: DIPR430685_05CLC\n"
                                +"Lớp: Xử lý ảnh số\n"
                                +"Tiết: 7 - 9 chiều thứ 2")
        self.mlhp_label.setFont(font)
        self.mlhp_label.adjustSize()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.run_script)
        self.exitButton.clicked.connect(self.stop_script)
        
    def __init__(self):
        super().__init__()
        self.process = None
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nhóm 11 - Nhận dạng khuôn mặt"))
        self.status_label.setText(_translate("MainWindow", ""))
        self.status_label.adjustSize()
    
    def run_script(self):
        script_path = 'main.py'
        if not os.path.isfile(script_path):
            QtWidgets.QMessageBox.critical(None, 'Error', 'File not found')
            return

        if os.path.isfile(script_path):
            self.status_label.setText("Running")
            self.status_label.adjustSize()
            self.exitButton.setVisible(True)
            self.process = QtCore.QProcess(self.centralwidget)
            self.process.start("python", [script_path])
            
    def stop_script(self):
        if self.process is not None:
            self.exitButton.setVisible(False)
            self.process.kill()
            self.status_label.setText("")
            self.status_label.adjustSize() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())
