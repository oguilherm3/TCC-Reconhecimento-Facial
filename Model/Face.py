from DAO import FaceDAO


class Face:
    def __init__(self, filename):
        self.filename = filename

    def insert_face(self):
        return FaceDAO.insert(self)