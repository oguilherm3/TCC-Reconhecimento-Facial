import cv2
import numpy as np
import face_recognition
import gridfs
from pymongo import MongoClient



db = MongoClient("mongodb+srv://unip:aluno@cluster0.c2q6lgv.mongodb.net/?retryWrites=true&w=majority") \
    .get_database("TCC")

fs = gridfs.GridFS(db, "Face")

path = './Resources/Temp/img.png'
images = []
nomesAlunos = []

for grid_data in fs.find():
    output = open(path, "wb")
    output.write(grid_data.read())
    curImg = cv2.imread(path)
    images.append(curImg)
    name = grid_data.__getattribute__('filename')
    name_list = name.split('.')[0]
    nomesAlunos.append(name_list)
print(f'classNames: {nomesAlunos}')


def findEncodins(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodeListKnown = findEncodins(images)
print(len(encodeListKnown))
print('Encoding complete')

camera = cv2.VideoCapture(0)

while True:
    success, imagem = camera.read()
    ImagemP = cv2.resize(imagem, (0, 0), None, 0.25, 0.25)
    ImagemP = cv2.cvtColor(ImagemP, cv2.COLOR_BGR2RGB)

    facesFrameAtual = face_recognition.face_locations(ImagemP)                  #find all locations in small image
    encodeFrameAtual = face_recognition.face_encodings(ImagemP, facesFrameAtual) #send the faces & its locations

    for encodeFace, faceLoc in zip(encodeFrameAtual, facesFrameAtual):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        print('matches', matches)
        distanciaFacial = face_recognition.face_distance(encodeListKnown, encodeFace)
        print('faceDis: ', distanciaFacial)
        indiceMatch = np.argmin(distanciaFacial)

        if matches[indiceMatch]:
            name = nomesAlunos[indiceMatch].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(imagem, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagem, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagem, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


    cv2.imshow('Webcam', imagem)
    cv2.waitKey(1)