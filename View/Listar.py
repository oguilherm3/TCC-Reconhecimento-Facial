# -*- coding: utf-8 -*-
from DAO import AlunoDAO
# Form implementation generated from reading ui file 'Listar2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from Model.Aluno import Aluno
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton, QComboBox, QLineEdit
import os


class Ui_ListWindow(object):

    def __init__(self, controller):
        self.listar = QtWidgets.QMainWindow()
        self.ui = Ui_ListWindow
        self.controller = controller
        self.ui.setupUi(self, self.listar)


    logo_path = os.getcwd().replace('Controller', 'Resources').replace('\\', '/') + '/Images/unip-logo.png'

    def setupUi(self, ListWindow):
        ListWindow.setObjectName("ListWindow")
        ListWindow.setFixedSize(1192, 727)
        ListWindow.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.centralwidget = QtWidgets.QWidget(ListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(-10, 0, 251, 91))
        self.lblLogo.setStyleSheet("image: url(" + self.logo_path + ");")
        self.lblLogo.setText("")
        self.lblLogo.setObjectName("lblLogo")
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(510, 20, 151, 51))
        self.btnRefreshTable = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefreshTable.setGeometry(QtCore.QRect(1090, 90, 75, 23))
        self.btnRefreshTable.setObjectName("btnRegister")
        self.btnRefreshTable.clicked.connect(self.monta_lista)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setObjectName("lblTitulo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 1151, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.alunos = list
        self.monta_lista()
        ListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastrar = QtWidgets.QMenu(self.menubar)
        self.menuCadastrar.setObjectName("menuCadastrar")
        ListWindow.setMenuBar(self.menubar)
        self.actionAlunoCadastro = QtWidgets.QAction(ListWindow)
        self.actionAlunoCadastro.setObjectName("actionAlunoCadastro")
        self.actionFuncionarioCadastro = QtWidgets.QAction(ListWindow)
        self.actionFuncionarioCadastro.setObjectName("actionFuncionarioCadastro")
        self.actionFuncionarioCadastro.setEnabled(False)
        self.actionAlunoCadastro.triggered.connect(self.cadastrar_screen)
        self.menuCadastrar.addAction(self.actionAlunoCadastro)
        self.menuCadastrar.addAction(self.actionFuncionarioCadastro)
        self.menubar.addAction(self.menuCadastrar.menuAction())

        self.retranslateUi(ListWindow)
        QtCore.QMetaObject.connectSlotsByName(ListWindow)

    def monta_lista(self):

        self.alunos = self.alunos_list()
        tabela = self.tableWidget
        # Dimensionando a tabela
        tabela.setColumnCount(7)
        tabela.setRowCount(len(self.alunos))

        # Opções das combo boxes
        cursos = self.cursos_list()
        campi = self.campi_list()

        # Definir cabeçalho da tabela
        tabela.setHorizontalHeaderLabels(['Nome', 'Curso', 'Campus', 'Telefone', '', '', ''])

        # Adicionar os dados à tabela
        for row_idx, row_data in enumerate(self.alunos):
            item_name = QTableWidgetItem(row_data['nome'])

            item_phone = QLineEdit()
            item_phone.setInputMask("(00) 00000 - 0000")
            item_phone.setText(str(row_data['phone']))

            item_course = QComboBox()
            item_course.addItems(cursos)
            item_course.addItem('')
            item_course.setCurrentText(str(row_data['course']))

            item_campus = QComboBox()
            item_campus.addItems(campi)
            item_campus.addItem('')
            item_campus.setCurrentText(str(row_data['campus']))

            btnAtualizar = QPushButton('Atualizar')
            btnAtualizar.clicked.connect(self.atualiza_Aluno)

            btnEditar = QPushButton('Editar')
            btnEditar.clicked.connect(self.editar_screen)
            item_editar = btnEditar

            btnDeletar = QPushButton('Deletar')
            btnDeletar.clicked.connect(self.deleta_Aluno)
            item_deletar = btnDeletar

            tabela.setItem(row_idx, 0, item_name)
            tabela.setCellWidget(row_idx, 1, item_course)
            tabela.setCellWidget(row_idx, 2, item_campus)
            tabela.setCellWidget(row_idx, 3, item_phone)
            tabela.setCellWidget(row_idx, 4, btnAtualizar)
            tabela.setCellWidget(row_idx, 5, item_editar)
            tabela.setCellWidget(row_idx, 6, item_deletar)

        # Redimensionar colunas
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def retranslateUi(self, ListWindow):
        _translate = QtCore.QCoreApplication.translate
        ListWindow.setWindowTitle(_translate("ListWindow", "Listar"))
        self.lblTitulo.setText(_translate("ListWindow", "Alunos"))
        self.menuCadastrar.setTitle(_translate("ListWindow", "Cadastrar"))
        self.actionAlunoCadastro.setText(_translate("RegisterWindow", "Aluno"))
        self.actionFuncionarioCadastro.setText(_translate("RegisterWindow", "Funcionário"))
        self.btnRefreshTable.setText(_translate("ListWindow", "Refresh"))

    def editar_screen(self):
        idx = self.tableWidget.currentRow()
        aluno = self.alunos[idx]

        self.controller.openEditScreen(aluno)

    def cadastrar_screen(self):
        self.controller.openCadastroScreen()

    def atualiza_Aluno(self):
        idx = self.tableWidget.currentRow()
        aluno = self.alunos[idx]

        nome = self.tableWidget.item(idx, 0).text()
        course = self.tableWidget.cellWidget(idx, 1).currentText()
        campus = self.tableWidget.cellWidget(idx, 2).currentText()
        phone = self.tableWidget.cellWidget(idx, 3).displayText()

        a = Aluno(nome, aluno['rg'], aluno['cpf'], aluno['birthDate'], course, campus, aluno['cep'],
                  aluno['address'], aluno['address_complement'], aluno['address_number'], aluno['address_city'], aluno['address_uf'],
                  aluno['face_id'], phone)

        self.controller.atualizar(a, self.centralwidget)

    def deleta_Aluno(self):
        idx = self.tableWidget.currentRow()
        aluno = self.alunos[idx]

        nome = self.tableWidget.item(idx, 0).text()
        course = self.tableWidget.cellWidget(idx, 1).currentText()
        campus = self.tableWidget.cellWidget(idx, 2).currentText()
        phone = self.tableWidget.cellWidget(idx, 3).displayText()

        a = Aluno(nome, aluno['rg'], aluno['cpf'], aluno['birthDate'], course, campus, aluno['cep'],
                  aluno['address'], aluno['address_complement'], aluno['address_number'], aluno['address_city'], aluno['address_uf'],
                  aluno['face_id'], aluno['phone'])

        self.controller.deletar(a, self.centralwidget)

    def alunos_list(self):
        return self.controller.getAlunos()

    def cursos_list(self):
        return self.controller.getCursos()

    def campi_list(self):
        return self.controller.getCampi()
# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ListarWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(ListarWindow)
#     ListarWindow.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()