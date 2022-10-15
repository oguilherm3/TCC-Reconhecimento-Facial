import cv2

def capture():

    cam = cv2.VideoCapture(0) # initializing webcam


    while True:
        success, img = cam.read()

        if not success:
            print('failed to grab frame')
            break

        cv2.imshow('Register', img)
        k = cv2.waitKey(1)   # setting a key to close the application

        if k%256 == 27: # checking for ESC key
            print('ESC hit, closing the app')
            break

        elif k%256 == 32: # cheking for the spacebar
            #img_name = 'opencv_frame_{}.png'.format(img_counter)
            #cv2.imwrite(img_name, img)
            print('Screeshot taken')
            #img_counter+=1
            break

    cam.release() # releasing camera

    cv2.destroyWindow('Register') # after we're finished destroy all windows

    return img