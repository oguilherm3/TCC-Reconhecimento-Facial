import os

import gridfs
from Connection.ConnectionFactory import ConnectionFactory


def insert(face):
    cur = os.getcwd().replace('View', 'Resources')
    path = cur.replace('\\', '/') + '/Temp/temp_photo.png'

    try:
        db = ConnectionFactory.getDatabase('TCC')
        fs = gridfs.GridFS(db, "Face")

        with open(path, 'rb') as f:
            file_id = fs.put(f.read(), filename=face.filename)
        return file_id
    except Exception as e:
        print('Error in mongo insert: ', e)