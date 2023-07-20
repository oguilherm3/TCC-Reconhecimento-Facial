import os


class Control:
    def __init__(self):
        self._cur = os.getcwd().replace('Controller', 'Resources')
        self.register_path = self._cur.replace('\\', '/') + '/Images/RegisterProfilePhoto.png'
        self.temp_path = self._cur.replace('\\', '/') + '/Temp/temp_photo.png'