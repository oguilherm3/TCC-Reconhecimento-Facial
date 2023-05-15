from Model.Pessoa import Pessoa
from DAO import AlunoDAO


def get_Alunos():
    return AlunoDAO.listaAlunos()


class Aluno(Pessoa):
    def __init__(self, _id, nome, rg, cpf, birthDate, course, campus, cep, address, address_complement, address_number, address_city, face_id, phone):  # Aluno Constructor
        super().__init__(nome, rg, cpf, birthDate)  # Pessoa Constructor
        self._id = _id
        self.course = course
        self.campus = campus
        self.cep = cep
        self.address = address
        self.address_complement = address_complement
        self.address_number = address_number
        self.address_city = address_city
        self.face_id = face_id
        self.phone = phone
        self.raGenerator()
        self.findFace()

    def raGenerator(self):
        pass

    def findFace(self):
        pass

    def insert_student(self):
        AlunoDAO.insert(self)

    def register_student(self, photo):
        aluno_id = AlunoDAO.insert_getId(self)

    def atualiza_student(self):
        return AlunoDAO.update(self)


