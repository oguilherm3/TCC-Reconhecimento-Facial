import cv2
import numpy as np
import face_recognition
import os
import serial
import asyncio

porta_serial = serial.Serial('COM4', 9600)  # Substitua 'COM3' pela porta serial correta


def ligar_led():
    porta_serial.write('liga\n'.encode())
    print(f'Comando para ligar o LED enviado.: {porta_serial.read()}')


def desligar_led():
    porta_serial.write('desliga\n'.encode())
    print('Comando para desligar o LED enviado.')


path = 'Resources/ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print('classNames', classNames)


def findEncodins(images):
    encodelist = []
    errorlist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
        except Exception as e:
            errorlist.append(img)
    return encodelist


encodeListKnown = findEncodins(images)
print('Encoding complete')

cap = cv2.VideoCapture(0)
condition = True
comando = ""
count = 0
while condition:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)  # find all locations in small image
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)  # send the faces & its locations

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        # print('matches', matches)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print('faceDis: ', faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            print("teste")
            if count < 4:
                ligar_led()
                count = count + 1
                print(count)

        # else:
        #     desligar_led()

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
# faceLoc = face_recognition.face_locations(imgGuilherme)[0] # top_right, bottom_right, top_left, bottom_left
# encodeGuilherme = face_recognition.face_encodings(imgGuilherme)[0]
# cv2.rectangle(imgGuilherme, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

# faceLocTest = face_recognition.face_locations(imgTest)[0] # top_right, bottom_right, top_left, bottom_left
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# results = face_recognition.compare_faces([encodeGuilherme], encodeTest)
# faceDis = face_recognition.face_distance([encodeGuilherme], encodeTest)
