# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listar2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from Model.Aluno import Aluno, get_Alunos
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton, QMessageBox, QWidget, \
    QComboBox, QLineEdit
import os

from Model.Campus import Campus
from Model.Curso import Curso


class Ui_MainWindow(object):
    logo_path = os.getcwd().replace('View', 'Resources').replace('\\', '/') + '/Images/unip-logo.png'
    alunos = get_Alunos()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1192, 727)
        MainWindow.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(-10, 0, 251, 91))
        self.lblLogo.setStyleSheet("image: url(" + self.logo_path + ");")
        self.lblLogo.setText("")
        self.lblLogo.setObjectName("lblLogo")
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(510, 20, 151, 51))
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
        self.monta_lista(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastrar = QtWidgets.QMenu(self.menubar)
        self.menuCadastrar.setObjectName("menuCadastrar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCadastrar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def monta_lista(self, tabela):

        # Dimensionando a tabela
        tabela.setColumnCount(6)
        tabela.setRowCount(len(self.alunos))

        # Opções das combo boxes
        cursos = Curso().get_lista()
        campi = Campus().get_lista()

        # Definir cabeçalho da tabela
        tabela.setHorizontalHeaderLabels(['Nome', 'Curso', 'Campus', 'Telefone', '', ''])

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
            btnEditar.clicked.connect(self.editaAluno)
            item_editar = btnEditar

            tabela.setItem(row_idx, 0, item_name)
            tabela.setCellWidget(row_idx, 1, item_course)
            tabela.setCellWidget(row_idx, 2, item_campus)
            tabela.setCellWidget(row_idx, 3, item_phone)
            tabela.setCellWidget(row_idx, 4, btnAtualizar)
            tabela.setCellWidget(row_idx, 5, item_editar)

        # Redimensionar colunas
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listar"))
        self.lblTitulo.setText(_translate("MainWindow", "Alunos"))
        self.menuCadastrar.setTitle(_translate("MainWindow", "Cadastrar"))

    def editaAluno(self):

        print('Editar aluno clicado')

    def atualiza_Aluno(self):
        idx = self.tableWidget.currentRow()
        filtro = self.alunos[idx].get("_id")
        aluno = self.alunos[idx]

        aluno['nome'] = self.tableWidget.item(idx, 0).text()
        aluno['course'] = self.tableWidget.cellWidget(idx, 1).currentText()
        aluno['campus'] = self.tableWidget.cellWidget(idx, 2).currentText()
        aluno['phone'] = self.tableWidget.cellWidget(idx, 3).displayText()

        resultado = Aluno.atualiza_student(Aluno(**aluno))

        if resultado:
            return QMessageBox.information(self.centralwidget, 'Sucesso', 'O Aluno foi atualizado com sucesso!')
        else:
            return QMessageBox.information(self.centralwidget, 'Falha', 'O Aluno não foi atualizado')

    def atualiza_lista(self):
        pass

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListarWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(ListarWindow)
    ListarWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()