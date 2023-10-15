from DAO import CampusDAO


def get_lista():
    return CampusDAO.listaCampi()


class Campus:
    def __init__(self):
        self.nome = str()

