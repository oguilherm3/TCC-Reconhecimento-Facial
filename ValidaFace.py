import cv2
import numpy as np
import face_recognition
import gridfs
import serial
from pymongo import MongoClient

db = MongoClient("mongodb+srv://unip:aluno@cluster0.c2q6lgv.mongodb.net/?retryWrites=true&w=majority") \
    .get_database("TCC")

fs = gridfs.GridFS(db, "Face")

path = './Resources/Temp/img.png'
images = []
nomesAlunos = []


def findEncodins(image_list):
    encodelist = []
    errorList = []
    for img in image_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # transformando a imagem em RGB
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodelist.append(encode)  # armazena as dimensões do rosto
        except Exception as e:
            errorList.append(img)
            print(f'Exception {e}')

    return encodelist

for photo in fs.find():
    output = open(path, "wb")
    output.write(photo.read())  # salva a face atual no diretório temporário para possibilitar o uso do opencv
    curImg = cv2.imread(path)  # usando o opencv para ler a imagem e armazenar em uma variável
    images.append(curImg)  # guarda a imagem em uma lista
    name = photo.__getattribute__('filename')  # armazena o nome da face atual
    name_list = name.split('.')[0]
    nomesAlunos.append(name_list)
print(f'classNames: {nomesAlunos}')

encodeListKnown = findEncodins(images)  # lista com todos os rostos conhecidos pelo sistema
print('Encoding complete')

camera = cv2.VideoCapture(0)

while True:
    success, imagem = camera.read()
    ImagemP = cv2.resize(imagem, (0, 0), None, 0.25,
                         0.25)  # reduz o tamanho da img para o reconhecimento ser mais rápido
    ImagemP = cv2.cvtColor(ImagemP, cv2.COLOR_BGR2RGB)

    facesFrameAtual = face_recognition.face_locations(ImagemP)  # find all locations in small image
    encodeFrameAtual = face_recognition.face_encodings(ImagemP, facesFrameAtual)  # send the faces & its locations

    print(f"FACES: {facesFrameAtual}")
    if facesFrameAtual:
        for encodeFace, faceLoc in zip(encodeFrameAtual, facesFrameAtual):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            # print('matches', matches)
            distanciaFacial = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print('faceDis: ', distanciaFacial)
            indiceMatch = np.argmin(distanciaFacial)

            if matches[indiceMatch]:
                name = nomesAlunos[indiceMatch].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(imagem, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(imagem, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(imagem, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Webcam', imagem)
    cv2.waitKey(1)
