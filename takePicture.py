import cv2
import os
def capture():

    cam = cv2.VideoCapture(0) # initializing webcam

    while True:
        success, img = cam.read()
        if not success:
            print('failed to grab frame')
            break

        cv2.imshow('Foto', img)
        k = cv2.waitKey(1)   # setting a key to close the application

        if k%256 == 27: # checking for ESC key
            print('ESC hit, closing the app')
            break

        elif k%256 == 32: # cheking for the spacebar
            print('Screeshot taken')
            break

    cam.release() # releasing camera
    cv2.destroyWindow('Foto') # after we're finished destroy the Register window

    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)