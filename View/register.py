# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(1045, 633)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frRegister = QtWidgets.QFrame(self.centralwidget)
        self.frRegister.setGeometry(QtCore.QRect(70, 70, 451, 451))
        self.frRegister.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frRegister.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frRegister.setObjectName("frRegister")
        self.lblName = QtWidgets.QLabel(self.frRegister)
        self.lblName.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(self.frRegister)
        self.txtName.setGeometry(QtCore.QRect(20, 90, 401, 20))
        self.txtName.setObjectName("txtName")
        self.txtRG = QtWidgets.QLineEdit(self.frRegister)
        self.txtRG.setGeometry(QtCore.QRect(20, 140, 181, 20))
        self.txtRG.setObjectName("txtRG")
        self.lblRG = QtWidgets.QLabel(self.frRegister)
        self.lblRG.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.lblRG.setObjectName("lblRG")
        self.lblCPF = QtWidgets.QLabel(self.frRegister)
        self.lblCPF.setGeometry(QtCore.QRect(220, 120, 47, 13))
        self.lblCPF.setObjectName("lblCPF")
        self.txtCPF = QtWidgets.QLineEdit(self.frRegister)
        self.txtCPF.setGeometry(QtCore.QRect(220, 140, 201, 20))
        self.txtCPF.setObjectName("txtCPF")
        self.lblPhone = QtWidgets.QLabel(self.frRegister)
        self.lblPhone.setGeometry(QtCore.QRect(20, 170, 47, 13))
        self.lblPhone.setObjectName("lblPhone")
        self.txtPhone = QtWidgets.QLineEdit(self.frRegister)
        self.txtPhone.setGeometry(QtCore.QRect(20, 190, 181, 20))
        self.txtPhone.setObjectName("txtPhone")
        self.lblBirthDate = QtWidgets.QLabel(self.frRegister)
        self.lblBirthDate.setGeometry(QtCore.QRect(220, 170, 101, 16))
        self.lblBirthDate.setObjectName("lblBirthDate")
        self.dateEdit = QtWidgets.QDateEdit(self.frRegister)
        self.dateEdit.setGeometry(QtCore.QRect(220, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.cbxUF = QtWidgets.QComboBox(self.frRegister)
        self.cbxUF.setGeometry(QtCore.QRect(220, 240, 61, 22))
        self.cbxUF.setObjectName("cbxUF")
        self.lblUF = QtWidgets.QLabel(self.frRegister)
        self.lblUF.setGeometry(QtCore.QRect(220, 220, 61, 16))
        self.lblUF.setObjectName("lblUF")
        self.txtCEP = QtWidgets.QLineEdit(self.frRegister)
        self.txtCEP.setGeometry(QtCore.QRect(20, 240, 181, 20))
        self.txtCEP.setObjectName("txtCEP")
        self.lblCEP = QtWidgets.QLabel(self.frRegister)
        self.lblCEP.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.lblCEP.setObjectName("lblCEP")
        self.txtComplement = QtWidgets.QLineEdit(self.frRegister)
        self.txtComplement.setGeometry(QtCore.QRect(20, 350, 401, 20))
        self.txtComplement.setObjectName("txtComplement")
        self.lblComplement = QtWidgets.QLabel(self.frRegister)
        self.lblComplement.setGeometry(QtCore.QRect(20, 330, 71, 16))
        self.lblComplement.setObjectName("lblComplement")
        self.txtAddress = QtWidgets.QLineEdit(self.frRegister)
        self.txtAddress.setGeometry(QtCore.QRect(20, 300, 401, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.lblAddress = QtWidgets.QLabel(self.frRegister)
        self.lblAddress.setGeometry(QtCore.QRect(20, 280, 47, 13))
        self.lblAddress.setObjectName("lblAddress")
        self.rdbStudent = QtWidgets.QRadioButton(self.frRegister)
        self.rdbStudent.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.rdbStudent.setObjectName("rdbStudent")
        #self.rdbStudent.toggled()
        self.rdnEmployee = QtWidgets.QRadioButton(self.frRegister)
        self.rdnEmployee.setGeometry(QtCore.QRect(150, 30, 82, 17))
        self.rdnEmployee.setObjectName("rdnEmployee")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(540, 70, 451, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 330))
        self.label.setStyleSheet("image: url(C:/Users/Guilherme/Downloads/PngItem_1503945.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(540, 460, 451, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lblCourse = QtWidgets.QLabel(self.frame_2)
        self.lblCourse.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.lblCourse.setObjectName("lblCourse")
        self.cbxCourse = QtWidgets.QComboBox(self.frame_2)
        self.cbxCourse.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.cbxCourse.setObjectName("cbxCourse")
        self.lblCampus = QtWidgets.QLabel(self.frame_2)
        self.lblCampus.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.lblCampus.setObjectName("lblCampus")
        self.cbxCampus = QtWidgets.QComboBox(self.frame_2)
        self.cbxCampus.setGeometry(QtCore.QRect(210, 30, 191, 22))
        self.cbxCampus.setObjectName("cbxCampus")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(700, 420, 151, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnPicture_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPicture_2.setObjectName("btnPicture_2")
        self.verticalLayout.addWidget(self.btnPicture_2)
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(470, 550, 91, 41))
        self.btnRegister.setObjectName("btnRegister")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.lblName.setText(_translate("RegisterWindow", "Nome: "))
        self.lblRG.setText(_translate("RegisterWindow", "RG:"))
        self.lblCPF.setText(_translate("RegisterWindow", "CPF: "))
        self.lblPhone.setText(_translate("RegisterWindow", "Telefone: "))
        self.lblBirthDate.setText(_translate("RegisterWindow", "Data Nascimento: "))
        self.lblUF.setText(_translate("RegisterWindow", "UF"))
        self.lblCEP.setText(_translate("RegisterWindow", "CEP"))
        self.lblComplement.setText(_translate("RegisterWindow", "Complemento"))
        self.lblAddress.setText(_translate("RegisterWindow", "Endereço: "))
        self.rdbStudent.setText(_translate("RegisterWindow", "Aluno"))
        self.rdnEmployee.setText(_translate("RegisterWindow", "Funcionário"))
        self.lblCourse.setText(_translate("RegisterWindow", "Curso: "))
        self.lblCampus.setText(_translate("RegisterWindow", "Unidade: "))
        self.btnPicture_2.setText(_translate("RegisterWindow", "Tirar Foto"))
        self.btnRegister.setText(_translate("RegisterWindow", "Cadastrar"))
#import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
