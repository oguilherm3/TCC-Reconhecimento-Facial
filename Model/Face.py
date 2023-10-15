from DAO import FaceDAO


def get_face_by_id(file_id):
    return FaceDAO.get_by_id(file_id)


def delete_face_by_id(file_id):
    return FaceDAO.delete_by_id(file_id)


class Face:
    def __init__(self, filename):
        self.filename = filename

    def insert_face(self):
        return FaceDAO.insert(self)
