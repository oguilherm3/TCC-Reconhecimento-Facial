import cv2

cam = cv2.VideoCapture(0) # initializing webcam

img_counter = 0

while True:
    success, frame = cam.read()

    if not success:
        print('failed to grab frame')
        break

    cv2.imshow('test', frame)
    k = cv2.waitKey(1)   # setting a key to close the application

    if k%256 == 27: # checking for ESC key
        print('ESC hit, closing the app')
        break

    elif k%256 == 32: # cheking for the spacebar
        img_name = 'opencv_frame_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print('Screeshot taken')
        img_counter+=1

cam.release() # releasing camera

cam.destroyAllWindows() # after we're finished destroy all windows