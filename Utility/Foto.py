import cv2


def capturar():
    cam = cv2.VideoCapture(0)  # Iniciliazando a camera

    while True:
        sucesso, img = cam.read()
        if not sucesso:
            print('falha ao capturar a camera')
            break

        cv2.imshow('Foto', img)
        k = cv2.waitKey(1)

        if k % 256 == 27:  # esperando pela tecla ESC
            # print('ESC, fechando')
            break

        elif k % 256 == 32:  # Esperando pela barra de espaço
            # print('Foto tirada')
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cam.release()
    cv2.destroyWindow('Foto')  # Depois terminado fechar a janela
