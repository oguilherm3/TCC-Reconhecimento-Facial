# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'RegisterV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtWidgets import QMessageBox

import takePicture
from datetime import date, datetime
from PIL import Image

from Connection.ConnectionFactory import ConnectionFactory
from Model.Aluno import Aluno
from Model.Curso import Curso
from Model.Campus import Campus
from Model.Face import Face


class Ui_RegisterWindow(object):
    def __init__(self, controller):
        self.cadastrar = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow
        self.ui.setupUi(self, self.cadastrar)
        self.controller = controller

    cursos = Curso().get_lista()
    campi = Campus().get_lista()

    def setupUi(self, RegisterWindow):

        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.setFixedSize(1045, 633)
        # RegisterWindow.setMenuBar() TODO: Review!
        RegisterWindow.setStyleSheet('background-color: rgb(255, 255, 255);')
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
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(date.fromisoformat("1900-01-01"))
        self.dateEdit.setMaximumDate(date.today())
        self.cbxUF = QtWidgets.QComboBox(self.frRegister)
        self.cbxUF.setGeometry(QtCore.QRect(360, 240, 61, 22))
        self.cbxUF.setObjectName("cbxUF")
        self.cbxUF.setDisabled(True)
        self.lblUF = QtWidgets.QLabel(self.frRegister)
        self.lblUF.setGeometry(QtCore.QRect(360, 220, 61, 16))
        self.lblUF.setObjectName("lblUF")
        self.txtCEP = QtWidgets.QLineEdit(self.frRegister)
        self.txtCEP.setGeometry(QtCore.QRect(20, 240, 181, 20))
        self.txtCEP.setObjectName("txtCEP")
        self.txtCEP.setInputMask("00000 - 000")
        self.txtCEP.setMaxLength(8)
        self.txtCEP.textEdited.connect(self.autoFillCep)
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
        # self.label.setStyleSheet("image: url(" + self.path + ");")
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
        self.cbxCourse.addItems(self.cursos)
        self.cbxCourse.setCurrentText('-')
        self.lblCampus = QtWidgets.QLabel(self.frame_2)
        self.lblCampus.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.lblCampus.setObjectName("lblCampus")
        self.cbxCampus = QtWidgets.QComboBox(self.frame_2)
        self.cbxCampus.setGeometry(QtCore.QRect(210, 30, 191, 22))
        self.cbxCampus.setObjectName("cbxCampus")
        self.cbxCampus.addItems(self.campi)
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
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(470, 550, 91, 41))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(self.register)
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(RegisterWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuCadastro = QtWidgets.QMenu(self.menuBar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuConsultar = QtWidgets.QMenu(self.menuBar)
        self.menuConsultar.setObjectName("menuConsultar")
        RegisterWindow.setMenuBar(self.menuBar)
        self.actionAlunoCadastro = QtWidgets.QAction(RegisterWindow)
        self.actionAlunoCadastro.setObjectName("actionAlunoCadastro")
        self.actionListarAlunos = QtWidgets.QAction(RegisterWindow)
        self.actionListarAlunos.setObjectName("actionListarAlunos")
        self.menuCadastro.addAction(self.actionAlunoCadastro)
        self.menuConsultar.addAction(self.actionListarAlunos)
        self.menuBar.addAction(self.menuCadastro.menuAction())
        self.menuBar.addAction(self.menuConsultar.menuAction())

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def takePicture(self):
        img = takePicture.capture()
        Image.fromarray(img).save(self.controller.temp_path)

        self.update_photo()

    def update_photo(self):
        self.label.setStyleSheet("image: url(" + self.controller.temp_path + ");")

    def register(self):
        a = Aluno(
            nome=self.txtName.displayText(), rg=self.txtRG.displayText(), cpf=self.txtCPF.displayText(),
            birthDate=str(self.dateEdit.dateTime().date().toPyDate()), course=self.cbxCourse.currentText(),
            campus=self.cbxCampus.currentText(), cep=self.txtCEP.displayText().strip(), address=self.txtAddress.displayText(),
            address_complement=self.txtComplement.displayText(), address_city=self.txtCity.displayText(),
            address_number=self.txtNumber.displayText(), address_uf=self.cbxUF.currentText(),
            face_id='', phone=self.txtPhone.displayText()
        )

        a.face_id = self.get_faceId(a.nome)

        self.controller.cadastrar(a, self.centralwidget)

    def verificaCep(self, cep):
        if not (len(cep) > 8 and cep != 'CEP Inválido'):
            self.btnRegister.setEnabled(False)
            return QMessageBox.warning(self.centralwidget, 'Aviso', 'CEP Inválido!')
        else:
            self.btnRegister.setEnabled(True)

    def get_faceId(self, aluno_nome):
        face = Face(
            filename=aluno_nome + '.png'
        )
        return face.insert_face()

    def autoFillCep(self):
        if len(self.txtCEP.text()) == 11:
            cep = self.txtCEP.text().replace('-', '').replace(' ', '')
            result = ConnectionFactory.getCep(cep)
            if result != 'Invalid':
                endereco = result["logradouro"] + ', ' + result["bairro"]
                uf = result["uf"]
                cidade = result["localidade"]
                self.txtAddress.setText(endereco)
                self.cbxUF.addItem(uf)
                self.txtCity.setText(cidade)
            else:
                self.txtAddress.setText('CEP Inválido')

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Cadastrar"))
        self.lblName.setText(_translate("RegisterWindow", "Nome: "))
        self.lblRG.setText(_translate("RegisterWindow", "RG:"))
        self.lblCPF.setText(_translate("RegisterWindow", "CPF: "))
        self.lblPhone.setText(_translate("RegisterWindow", "Telefone: "))
        self.lblBirthDate.setText(_translate("RegisterWindow", "Data de Nascimento: "))
        self.lblUF.setText(_translate("RegisterWindow", "UF"))
        self.lblCEP.setText(_translate("RegisterWindow", "CEP"))
        self.lblComplement.setText(_translate("RegisterWindow", "Complemento"))
        self.lblAddress.setText(_translate("RegisterWindow", "Endereço: "))
        self.rdbStudent.setText(_translate("RegisterWindow", "Aluno"))
        self.rdnEmployee.setText(_translate("RegisterWindow", "Funcionário"))
        self.lblNumber.setText(_translate("RegisterWindow", "Número: "))
        self.lblCity.setText(_translate("RegisterWindow", "Cidade:"))
        self.lblCourse.setText(_translate("RegisterWindow", "Curso: "))
        self.lblCampus.setText(_translate("RegisterWindow", "Unidade: "))
        self.btnPicture.setText(_translate("RegisterWindow", "Tirar Foto"))
        self.btnRegister.setText(_translate("RegisterWindow", "Cadastrar"))
        # self.menuCadastro.setTitle(_translate("RegisterWindow", "Cadastrar"))
        # self.menuConsultar.setTitle(_translate("RegisterWindow", "Listar"))
        # self.actionAlunoCadastro.setText(_translate("RegisterWindow", "Aluno"))
        # self.actionListarAlunos.setText(_translate("RegisterWindow", "Alunos"))


# import img_rc

# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     RegisterWindow = QtWidgets.QMainWindow()
#     ui = Ui_RegisterWindow()
#     ui.setupUi(RegisterWindow)
#     RegisterWindow.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()
