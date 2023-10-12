import os

from Controller.Control import Control
from Model.Face import Face, get_face_by_id, delete_face_by_id
from Model.Aluno import Aluno
from View.Editar import Ui_EditWindow
from Connection.ConnectionFactory import ConnectionFactory
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class EditarController(Control):
    def __init__(self, aluno):
        super().__init__()
        self.tela = Ui_EditWindow(self)
        self.aluno = aluno

    def show(self):
        if self.aluno['face_id'] != '':
            self.tela.aluno = self.aluno
            get_face_by_id(self.aluno['face_id'])
            self.tela.label.setStyleSheet("image: url(" + self.temp_path + ");")
            self.tela.ui.autoFillAluno(self.tela, self.tela.aluno)
            self.tela.editar.show()
        else:
            self.tela.label.setStyleSheet("image: url(" + self.register_path + ");")
            self.tela.editar.show()
            QMessageBox.information(self.tela.centralwidget, 'Aviso', 'O Aluno não possui uma foto '
                                                                      'cadastrada')

    def editar(self):
        nome = self.tela.txtName.text()
        rg = self.tela.txtRG.text()
        cpf = self.tela.txtCPF.text()
        birthDate = str(self.tela.dateEdit.dateTime().date().toPyDate())
        course = self.tela.cbxCourse.currentText()
        campus = self.tela.cbxCampus.currentText()
        cep = self.tela.txtCEP.displayText().strip()
        address = self.tela.txtAddress.displayText()
        address_complement = self.tela.txtComplement.displayText()
        address_city = self.tela.txtCity.displayText()
        address_number = self.tela.txtNumber.displayText()
        address_uf = self.tela.cbxUF.currentText()
        phone = self.tela.txtPhone.displayText()
        face_id = self.tela.aluno['face_id']

        a = Aluno(nome, rg, cpf, birthDate, course, campus, cep,
                  address, address_complement, address_number, address_city, address_uf,
                  face_id, phone)

        if self.tela.btnEdit.isEnabled():
            resultado = a.atualiza_student()
        else:
            resultado = False

        if resultado:
            return QMessageBox.information(self.tela.centralwidget, 'Sucesso', 'O Aluno foi atualizado com sucesso!')
        else:
            return QMessageBox.warning(self.tela.centralwidget, 'Aviso', 'Revise os dados do Aluno!')

    def editar_photo(self, face_id):

        resposta = QMessageBox.question(self.tela.centralwidget, 'Alerta!', f'Deseja atualizar a foto?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if resposta == QMessageBox.Yes:

            # a = Aluno()
            # pegar a foto atual e excluir
            delete_face_by_id(face_id)
            # inserir a nova foto e atualizar o id no aluno
            face = Face(
                    filename=self.aluno['nome'] + ".png"
            )

            res_id = face.insert_face()

            if res_id != False:
                self.aluno['face_id'] = res_id
                if Aluno.atualiza_student(self.aluno):
                    return QMessageBox.information(self.tela.centralwidget, 'Sucesso',
                                                   'A foto do aluno foi atualizada')
                else:
                    return QMessageBox.warning(self.tela.centralwidget, 'Falha',
                                               'Houve um erro ao cadastrar a foto do aluno')
            else:
                return QMessageBox.warning(self.tela.centralwidget, 'Falha',
                                           'Houve um erro ao cadastrar a foto do aluno')

    def valida_cep(self):
        cep = self.tela.txtCEP.text()
        if len(cep) == 11:
            cep_format = cep.replace('-', '').replace(' ', '')
            result = ConnectionFactory.getCep(cep_format)
            if result != 'Invalid':
                endereco = result["logradouro"] + ', ' + result["bairro"]
                uf = result["uf"]
                cidade = result["localidade"]
                self.tela.txtAddress.setText(endereco)
                self.tela.cbxUF.addItem(uf)
                self.tela.txtCity.setText(cidade)
                self.tela.btnEdit.setEnabled(True)
                return True
            else:
                self.tela.txtAddress.setText('CEP Inválido')
                self.tela.btnEdit.setEnabled(False)
                return QMessageBox.warning(self.tela.centralwidget, 'Aviso', 'Revise os dados do Aluno!')
