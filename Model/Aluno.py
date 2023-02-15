from Model.Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, rg, cpf, face):  # Aluno Constructor
        super().__init__(nome, rg, cpf)  # Pessoa Constructor
        self.course = ''
        self.campus = ''
        self.cep = ''
        self.address = ''
        self.complement = ''
        self.face = face
        self.phone = ''
        self.raGenerator()
        self.findFace()

    def raGenerator(self):
        pass

    def findFace(self):
        pass

    def register_student(self):
        AlunoDAO.insert(self)