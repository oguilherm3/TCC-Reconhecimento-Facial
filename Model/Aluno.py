from Model.Pessoa import Pessoa
from DAO import AlunoDAO
class Aluno(Pessoa):
    def __init__(self, nome, rg, cpf, face):  # Aluno Constructor
        super().__init__(nome, rg, cpf)  # Pessoa Constructor
        self.course = str()
        self.campus = str()
        self.cep = str()
        self.address = str()
        self.complement = str()
        self.face = face # list()
        self.phone = str()
        self.raGenerator()
        self.findFace()

    def raGenerator(self):
        pass

    def findFace(self):
        pass

    def register_student(self):
        AlunoDAO.insert(self)