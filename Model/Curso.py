from DAO import CursoDAO


def get_lista():
    return CursoDAO.listaCursos()


class Curso:
    def __init__(self):
        self.nome = str()
