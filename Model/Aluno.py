from Model.Pessoa import Pessoa
from DAO import AlunoDAO


class Aluno(Pessoa):
    def __init__(self, nome, rg, cpf, birthDate):  # Aluno Constructor
        super().__init__(nome, rg, cpf, birthDate)  # Pessoa Constructor
        self.id = str()
        self.course = str()
        self.campus = str()
        self.cep = str()
        self.address = str()
        self.address_complement = str()
        self.address_number = str()
        self.address_city = str()
        self.face_id = str()
        self.phone = str()
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

    def get_lista(self):
        return AlunoDAO.listaAlunos()

    def atualiza_student(self, aluno_atualizado):
        return AlunoDAO.update(aluno_atualizado)
