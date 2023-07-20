from PyQt5.QtWidgets import QMessageBox

from Controller.Control import Control
from Model.Aluno import Aluno
from Model.Face import Face
from View.Cadastro import Ui_RegisterWindow


class CadastrarController(Control):
    def __init__(self):
        super().__init__()
        self.tela = Ui_RegisterWindow(self)
        self.tela.label.setStyleSheet("image: url(" + self.register_path + ");")

    def show(self):
        self.tela.cadastrar.show()

    def cadastrar(self, aluno):
        # Inserir aluno sem face
        resultado = Aluno.insert_student(aluno)

        if resultado:
            # Inserir a face
            face = Face(
                filename=aluno.nome + ".png"
            )
            resultado = face.insert_face()  # resultado = face_id
            if resultado:
                # pegar o id e atualizar o field no aluno
                aluno.face_id = resultado
                Aluno.atualiza_student(aluno)
                return QMessageBox.information(self.tela.centralwidget, 'Sucesso',
                                               'O Aluno foi cadastrado com sucesso!')
            else:
                return QMessageBox.warning(self.tela.centralwidget, 'Falha',
                                           'Houve um erro ao cadastrar a foto do aluno')
        else:
            return QMessageBox.warning(self.tela.centralwidget, 'Falha', 'O Aluno não foi cadastrado')
