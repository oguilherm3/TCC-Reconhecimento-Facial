from Model.Pessoa import Pessoa
from DAO import AlunoDAO


def get_Alunos():
    return AlunoDAO.listaAlunos()


class Aluno(Pessoa):
    def __init__(self, nome, rg, cpf, birthDate, course, campus, cep, address, address_complement, address_number, address_city, address_uf, face_id, phone):  # Aluno Constructor
        super().__init__(nome, rg, cpf, birthDate)  # Pessoa Constructor
        self.course = course
        self.campus = campus
        self.cep = cep
        self.address = address
        self.address_complement = address_complement
        self.address_number = address_number
        self.address_city = address_city
        self.address_uf = address_uf
        self.face_id = face_id
        self.phone = phone

    def raGenerator(self):
        pass

    def findFace(self):
        pass

    def insert_student(self):
        return AlunoDAO.insert(self)

    def register_student(self, aluno):
        aluno_id = AlunoDAO.insert_getId(aluno)
        return aluno_id

    def atualiza_student(self):
        return AlunoDAO.update(self)

    def delete_student(self):
        return AlunoDAO.delete(self)


