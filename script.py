import cv2   #importação de módulos do OpenCV

camera = cv2.VideoCapture(0)    # seleção da câmara a utilizar

if __name__ == '__main__':  # quando se corre somente este ficheiro,  
    while True:             # entra-se em loop infinito
        ret, frame = camera.read()   # leitura da câmara digital
        if ret is True:              # se a leitura retornar TRUE, então:
            roi = frame[250:300, 0:640]  # definição de uma região de interesse a patir da variável "frame"
            
            cv2.imshow('frame', frame)   # vizualziação gráfica da imagem capturada pela câmara digital
            if cv2.waitKey(1) & 0xFF == ord('s'):   # pressionar 's' para sair (condição de saída)
                break
        else:                        # se a leitura retornar FALSE / interrumpida ---> quebra do ciclo
            print('Câmara não detectada')
            break
            
camera.release()   # libertação de recursos gráficos
cv2.destroyAllWindows() # comando para fechar definitivamente as interfaces do Raspberry Pi
