# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'RegisterV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

import takePicture
from datetime import date
from PIL import Image

from Connection.ConnectionFactory import ConnectionFactory
from Model.Aluno import Aluno


class Ui_EditWindow(object):

    def __init__(self, controller):
        self.editar = QtWidgets.QMainWindow()
        self.controller = controller
        self.ui = Ui_EditWindow
        self.ui.setupUi(self, self.editar)
        self.aluno = Aluno('', '', '', '', '', '', '', '', '', '', '', '', '', '')

    def setupUi(self, EditWindow):

        EditWindow.setObjectName("EditWindow")
        EditWindow.setFixedSize(1045, 633)
        EditWindow.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.centralwidget = QtWidgets.QWidget(EditWindow)
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
        self.txtRG.setInputMask("00.000.000 - >N")
        self.lblRG = QtWidgets.QLabel(self.frRegister)
        self.lblRG.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.lblRG.setObjectName("lblRG")
        self.lblCPF = QtWidgets.QLabel(self.frRegister)
        self.lblCPF.setGeometry(QtCore.QRect(220, 120, 47, 13))
        self.lblCPF.setObjectName("lblCPF")
        self.txtCPF = QtWidgets.QLineEdit(self.frRegister)
        self.txtCPF.setGeometry(QtCore.QRect(220, 140, 201, 20))
        self.txtCPF.setObjectName("txtCPF")
        self.txtCPF.setMaxLength(14)
        self.txtCPF.setInputMask("000.000.000 - 00")
        self.lblPhone = QtWidgets.QLabel(self.frRegister)
        self.lblPhone.setGeometry(QtCore.QRect(20, 170, 47, 13))
        self.lblPhone.setObjectName("lblPhone")
        self.txtPhone = QtWidgets.QLineEdit(self.frRegister)
        self.txtPhone.setGeometry(QtCore.QRect(20, 190, 181, 20))
        self.txtPhone.setObjectName("txtPhone")
        self.txtPhone.setInputMask("(00) 00000 - 0000")
        self.lblBirthDate = QtWidgets.QLabel(self.frRegister)
        self.lblBirthDate.setGeometry(QtCore.QRect(220, 170, 101, 16))
        self.lblBirthDate.setObjectName("lblBirthDate")
        self.dateEdit = QtWidgets.QDateEdit(self.frRegister)
        self.dateEdit.setGeometry(QtCore.QRect(220, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(date.fromisoformat("1900-01-01"))
        self.dateEdit.setMaximumDate(date.today())
        self.cbxUF = QtWidgets.QComboBox(self.frRegister)
        self.cbxUF.setGeometry(QtCore.QRect(360, 240, 61, 22))
        self.cbxUF.setObjectName("cbxUF")
        self.cbxUF.setEnabled(False)
        self.lblUF = QtWidgets.QLabel(self.frRegister)
        self.lblUF.setGeometry(QtCore.QRect(360, 220, 61, 16))
        self.lblUF.setObjectName("lblUF")
        self.txtCEP = QtWidgets.QLineEdit(self.frRegister)
        self.txtCEP.setGeometry(QtCore.QRect(20, 240, 181, 20))
        self.txtCEP.setObjectName("txtCEP")
        self.txtCEP.setInputMask("00000 - 000")
        self.txtCEP.setMaxLength(8)
        self.txtCEP.textEdited.connect(self.controller.valida_cep)
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
        self.txtAddress.setGeometry(QtCore.QRect(20, 300, 310, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.txtAddress.setDisabled(True)
        self.lblAddress = QtWidgets.QLabel(self.frRegister)
        self.lblAddress.setGeometry(QtCore.QRect(20, 280, 47, 13))
        self.lblAddress.setObjectName("lblAddress")
        self.rdbStudent = QtWidgets.QRadioButton(self.frRegister)
        self.rdbStudent.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.rdbStudent.setObjectName("rdbStudent")
        self.rdbStudent.setChecked(True)
        self.rdnEmployee = QtWidgets.QRadioButton(self.frRegister)
        self.rdnEmployee.setGeometry(QtCore.QRect(150, 30, 82, 17))
        self.rdnEmployee.setObjectName("rdnEmployee")
        self.rdnEmployee.setDisabled(True)
        self.txtNumber = QtWidgets.QLineEdit(self.frRegister)
        self.txtNumber.setGeometry(QtCore.QRect(360, 300, 61, 20))
        self.txtNumber.setObjectName("txtNumber")
        self.txtNumber.setMaxLength(5)
        self.lblNumber = QtWidgets.QLabel(self.frRegister)
        self.lblNumber.setGeometry(QtCore.QRect(360, 280, 47, 13))
        self.lblNumber.setObjectName("lblNumber")
        self.lblCity = QtWidgets.QLabel(self.frRegister)
        self.lblCity.setGeometry(QtCore.QRect(220, 220, 71, 16))
        self.lblCity.setObjectName("lblCity")
        self.txtCity = QtWidgets.QLineEdit(self.frRegister)
        self.txtCity.setGeometry(QtCore.QRect(220, 240, 111, 20))
        self.txtCity.setText("")
        self.txtCity.setDisabled(True)
        self.txtCity.setObjectName("txtCity")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(540, 70, 451, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 330))
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(540, 460, 451, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        cursos = self.controller.getCursos()
        self.lblCourse = QtWidgets.QLabel(self.frame_2)
        self.lblCourse.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.lblCourse.setObjectName("lblCourse")
        self.cbxCourse = QtWidgets.QComboBox(self.frame_2)
        self.cbxCourse.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.cbxCourse.setObjectName("cbxCourse")
        self.cbxCourse.addItems(cursos)
        self.cbxCourse.setCurrentText('-')
        self.lblCampus = QtWidgets.QLabel(self.frame_2)
        self.lblCampus.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.lblCampus.setObjectName("lblCampus")
        campi = self.controller.getCampi()
        self.cbxCampus = QtWidgets.QComboBox(self.frame_2)
        self.cbxCampus.setGeometry(QtCore.QRect(210, 30, 191, 22))
        self.cbxCampus.setObjectName("cbxCampus")
        self.cbxCampus.addItems(campi)
        self.cbxCampus.setCurrentText('-')
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(700, 420, 151, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnPicture = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPicture.setObjectName("btnPicture")
        self.btnPicture.clicked.connect(self.takePicture)
        self.verticalLayout.addWidget(self.btnPicture)
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(470, 550, 91, 41))
        self.btnEdit.setObjectName("btnRegister")
        self.btnEdit.clicked.connect(self.controller.editar)
        EditWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditWindow)
        QtCore.QMetaObject.connectSlotsByName(EditWindow)

    def takePicture(self):
        img = takePicture.capture()
        Image.fromarray(img).save(self.controller.temp_path)

        self.update_photo()

    def update_photo(self):
        self.label.setStyleSheet("image: url(" + self.controller.temp_path + ");")
        self.controller.editar_photo(self.aluno['face_id']) # investigar porque está vindo como dict aqui

    def autoFillAluno(self, aluno):
        self.aluno = aluno
        self.txtName.setText(aluno['nome'])
        self.txtRG.setText(aluno['rg'])
        self.txtCPF.setText(aluno['cpf'])
        self.dateEdit.setDate(date.fromisoformat(aluno['birthDate'])),
        self.cbxCourse.setCurrentText(aluno['course'])
        self.cbxCampus.setCurrentText(aluno['campus'])
        self.txtCEP.setText(aluno['cep'])
        self.txtAddress.setText(aluno['address'])
        self.txtComplement.setText(aluno['address_complement'])
        self.txtCity.setText(aluno['address_city'])
        self.txtNumber.setText(aluno['address_number'])
        self.cbxUF.addItem(aluno['address_uf'])
        self.txtPhone.setText(aluno['phone'])

    def retranslateUi(self, EditWindow):
        _translate = QtCore.QCoreApplication.translate
        EditWindow.setWindowTitle(_translate("EditWindow", "Editar"))
        self.lblName.setText(_translate("EditWindow", "Nome: "))
        self.lblRG.setText(_translate("EditWindow", "RG:"))
        self.lblCPF.setText(_translate("EditWindow", "CPF: "))
        self.lblPhone.setText(_translate("EditWindow", "Telefone: "))
        self.lblBirthDate.setText(_translate("EditWindow", "Data de Nascimento: "))
        self.lblUF.setText(_translate("EditWindow", "UF"))
        self.lblCEP.setText(_translate("EditWindow", "CEP"))
        self.lblComplement.setText(_translate("EditWindow", "Complemento"))
        self.lblAddress.setText(_translate("EditWindow", "Endereço: "))
        self.rdbStudent.setText(_translate("EditWindow", "Aluno"))
        self.rdnEmployee.setText(_translate("EditWindow", "Funcionário"))
        self.lblNumber.setText(_translate("EditWindow", "Número: "))
        self.lblCity.setText(_translate("EditWindow", "Cidade:"))
        self.lblCourse.setText(_translate("EditWindow", "Curso: "))
        self.lblCampus.setText(_translate("EditWindow", "Unidade: "))
        self.btnPicture.setText(_translate("EditWindow", "Tirar Foto"))
        self.btnEdit.setText(_translate("EditWindow", "Atualizar"))

# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     EditWindow = QtWidgets.QMainWindow()
#     ui = Ui_EditWindow()
#     ui.setupUi(EditWindow)
#     EditWindow.show()
#
#
# if __name__ == "__main__":
#     main()
