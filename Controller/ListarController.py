import os


from Model import Face
import EditarController
import CadastrarController
from Controller.Control import Control
from View.Listar import Ui_ListWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import sys


class ListarController(Control):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.telaPrincipal = Ui_ListWindow(self)
        self.telaPrincipal.listar.show()

    def openEditScreen(self, aluno):
        tela_editar = EditarController.EditarController(aluno)
        tela_editar.show()

    def openCadastroScreen(self):
        tela_cadastrar = CadastrarController.CadastrarController().show()

    def atualizar(self, aluno, widget):

        resultado = aluno.atualiza_student()

        if resultado:
            return QMessageBox.information(widget, 'Sucesso', 'O Aluno foi atualizado com sucesso!')
        else:
            return QMessageBox.information(widget, 'Falha', 'O Aluno não foi atualizado')

    def deletar(self, aluno, widget):

        resposta = QMessageBox.question(widget, 'Alerta!', f'Deseja continuar mesmo deletar o aluno: {aluno.nome}?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if resposta == QMessageBox.Yes:

            resultado_face = Face.delete_face_by_id(aluno.face_id)
            resultado_aluno = aluno.delete_student()

            if resultado_face and resultado_aluno:
                QMessageBox.information(widget, 'Sucesso', 'O Aluno foi deletado com sucesso!')
                return self.telaPrincipal.monta_lista()
            else:
                return QMessageBox.information(widget, 'Falha', 'Houve um problema na deleção')
        else:
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
