import cv2

camera = cv2.VideoCapture(0)  # leitura da câmara


if __name__ == '__main__':   
    while True:
        ret, frame = camera.read()  
        if ret is True:
            roi = frame[250:300, 0:640]


            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            print('Câmara não detectada')
            break
        
camera.release()
cv2.destroyAllWindows()