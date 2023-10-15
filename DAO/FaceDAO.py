import os

import gridfs
from Connection.ConnectionFactory import ConnectionFactory


def insert(face):
    cur = os.getcwd().replace('Controller', 'Resources')
    path = cur.replace('\\', '/') + '/Temp/temp_photo.png'

    try:
        db = ConnectionFactory.getDatabase('TCC')
        fs = gridfs.GridFS(db, "Face")

        with open(path, 'rb') as f:
            file_id = fs.put(f.read(), filename=face.filename)
        return file_id
    except Exception as e:
        print('Error in mongo insert: ', e)
        return False

def delete_by_id(file_id):
    try:
        db = ConnectionFactory.getDatabase('TCC')
        fs = gridfs.GridFS(db, "Face")

        fs.delete(file_id)
        return True

    except Exception as e:
        print('Error in mongo delete (Face): ', e)
        return False


def get_by_id(file_id):
    cur = os.getcwd().replace('Controller', 'Resources')
    path = cur.replace('\\', '/') + '/Temp/temp_photo.png'

    print(f'path {path}')

    db = ConnectionFactory.getDatabase('TCC')
    fs = gridfs.GridFS(db, "Face")

    try:
        db = ConnectionFactory.getDatabase('TCC')
        fs = gridfs.GridFS(db, "Face")

        with open(path, 'wb') as f:
            file = fs.get(file_id)
            f.write(file.read())
        return 'Success'
    except Exception as e:
        print('Error in mongo insert: ', e)
