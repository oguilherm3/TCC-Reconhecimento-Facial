from DAO import CursoDAO


class Curso:
    def __init__(self):
        self.nome = str()

    def get_lista(self):
        return CursoDAO.listaCursos()
