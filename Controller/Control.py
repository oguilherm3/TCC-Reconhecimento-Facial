import os

from PyQt5.QtWidgets import QMessageBox
from Model import Campus, Curso

class Control:
    def __init__(self):
        self._cur = os.getcwd().replace('Controller', 'Resources')
        self.register_path = self._cur.replace('\\', '/') + '/Images/RegisterProfilePhoto.png'
        self.temp_path = self._cur.replace('\\', '/') + '/Temp/temp_photo.png'

    def getCursos(self):
        return Curso.get_lista()

    def getCampi(self):
        return Campus.get_lista()

