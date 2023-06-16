from View import Editar
from View.Editar import Ui_EditWindow
from View.Listar import Ui_ListWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

class ListarController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.telaPrincipal = Ui_ListWindow(self)
        self.telaSecundaria = Ui_EditWindow(self)
        self.telaPrincipal.listar.show()

    def openEditScreen(self, aluno):
        self.telaSecundaria.aluno = aluno
        self.telaSecundaria.ui.autoFillAluno(self.telaSecundaria, self.telaSecundaria.aluno)
        self.telaSecundaria.editar.show()

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
