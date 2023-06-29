import os

from Model import Face
from View import Editar
from View.Cadastro import Ui_RegisterWindow
from View.Editar import Ui_EditWindow
from View.Listar import Ui_ListWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import sys

class ListarController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.telaPrincipal = Ui_ListWindow(self)
        self.telaSecundaria = Ui_EditWindow(self)
        self.telaCadastro = Ui_RegisterWindow(self)
        self.telaPrincipal.listar.show()

    def openEditScreen(self, aluno):
        cur = os.getcwd().replace('Controller', 'Resources')
        path = cur.replace('\\', '/') + '/Temp/temp_photo.png'
        if aluno['face_id'] != '':
            self.telaSecundaria.aluno = aluno
            Face.get_face_by_id(aluno['face_id'])
            self.telaSecundaria.label.setStyleSheet("image: url(" + path + ");")
            self.telaSecundaria.ui.autoFillAluno(self.telaSecundaria, self.telaSecundaria.aluno)
            self.telaSecundaria.editar.show()
        else:
            return QMessageBox.information(self.telaPrincipal.centralwidget, 'Falha', 'O Aluno não possui uma foto '
                                                                                      'cadastrada')

    def openCadastroScreen(self):
        cur = os.getcwd().replace('Controller', 'Resources')
        path = cur.replace('\\', '/') + '/Images/RegisterProfilePhoto.png'
        self.telaCadastro.label.setStyleSheet("image: url(" + path + ");")
        self.telaCadastro.cadastrar.show()
    def editarAluno(self):
        pass

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    controller = ListarController()
    controller.run()

# class ListarController:
#     def __init__(self):
#         self.tela_editar = Editar
#
#     def openEditScreen(self, aluno):
#         self.tela_editar.main()
#         self.tela_editar.Ui_EditWindow.autoFillAluno(Ui_EditWindow(), aluno)
