from DAO import CampusDAO

class Campus:
    def __init__(self):
        self.nome = str()

    def get_lista(self):
        return CampusDAO.listaCampi()