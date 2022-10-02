import cv2
import numpy as np
import face_recognition

imgGuilherme = face_recognition.load_image_file('ImageBasic/guilherme.jpeg')
imgGuilherme = cv2.cvtColor(imgGuilherme, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImageBasic/Bill gates.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Finding faces and Encoding
faceLoc = face_recognition.face_locations(imgGuilherme)[0] # top_right, bottom_right, top_left, bottom_left
encodeGuilherme = face_recognition.face_encodings(imgGuilherme)[0]
cv2.rectangle(imgGuilherme, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0] # top_right, bottom_right, top_left, bottom_left
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeGuilherme], encodeTest)
faceDis = face_recognition.face_distance([encodeGuilherme], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('Guilherme Test', imgTest)
cv2.imshow('Guilherme', imgGuilherme)
cv2.waitKey(0)