import numpy as np
import cv2 as cv
import datetime

camera = cv.VideoCapture(0) # captura a camera
car_cascade = cv.CascadeClassifier("treinamento/cascade.xml")
cascade = cv.CascadeClassifier("models/haarcascade_frontalface_default.xml")
contador = 1

def DetectCloseWindow(): # função utilizada fechar a aplicação
    lower_green = np.array([81, 146, 67], np.uint8)# gera a cor laranja de com a tonalidade mais baixa de acordo com a imagem
    upper_green = np.array([102, 255, 255], np.uint8)# gera a cor laranja de com a tonalidade mais alta de acordo com a imagem
    green_mask = cv.inRange(hsv_frame, lower_green, upper_green)# Pega a tonalidade da imagem HSV convertida entre lower_orange e upper_orange criando uma máscara em preto e branco
    result = cv.bitwise_and(frame, frame, mask=green_mask)# Através da imagem original em relação à máscara, essa váriavel vai retirar da imagem original o que não é de interesse
    frame_gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)# Converte a imagem do resultado para tons de cinza


    _, thresh = cv.threshold(frame_gray, 3, 255, cv.THRESH_BINARY)# aplica tecnica threshold
    contours, _ = cv.findContours(
        thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)#identifica os contornos na imagem
    
    for contour in contours:# percorre o array de contornos identificados
        area = cv.contourArea(contour)# pega o contorno da area
        if area > 1000:#testa o tamanho da area em pixels
            cv.putText(frame, "Green detected", (10, 80),# insere o texto com a cor identificada
                        cv.FONT_HERSHEY_SIMPLEX, 1, 1)# define as propriedades de estilo do texto
            cv.destroyAllWindows() # encerra a janela
            camera.release() # desativa a camera

def images():
    car_cascade = cv.CascadeClassifier("treinamento/cascade.xml")
    img = cv.imread("teste/teste(1).jpg")#le a imagem
    imagem = cv.imread("teste/teste(1).jpg",0)

    height, width = img.shape[:2]
    res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

    cv.imshow("aumento:", res)

    kernel = np.ones((5,5),np.uint8)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    objetos = car_cascade.detectMultiScale(gray, 1.2, 8)#detectar aquivo de treinamento
    print(objetos)
    for (x,y,w,h) in objetos:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #colocar retangulo nos pontos detectado
        imfImportant = gray[y:y+h, x:x+w ]#recorta ponto de interesse
        cv.imshow("Interesse", imfImportant)#imprime ponto de interesse
        cv.imwrite("recorte/imagem.jpg", imfImportant)#armazenar recorte da imagem

    opening = cv.morphologyEx(imagem, cv.MORPH_OPEN, kernel) #remove ruidos de fora da imagem

    closing = cv.morphologyEx(imagem, cv.MORPH_CLOSE, kernel)#remove ruidos de dentro da imagem

    cv.imshow('Analise', img)#imprimir imagem original na camera

    cv.imshow("Opening", opening)#mostra imagem sem ruidos por fora

    cv.imshow("closing", closing)#mostra imagem sem ruidos por dentro

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)#coloca a marcação de retangulo
    cv.imshow("cinza", gray)#mostra a imagem

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)#coloca a marcação de retangulo
    cv.imshow("HSV", hsv)#mostra a imagem

    blur = cv.GaussianBlur(gray, (7,7), 0)#embaça um pouco a imagem
    cv.imshow("Blur", blur)#mostra a imagem

    adaptativo = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 5)#adapta a imagem para ficar em preto e branco
    cv.imshow("Binario", adaptativo)#mostra a imagem

    cv.waitKey(0)


images()

while True:

    ret, frame = camera.read()#le a camera
    height, width, c = frame.shape#regula
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
     # (Imagem Gray, escala, qt. vizinhos)
    detect = cascade.detectMultiScale(gray, 1.2, 5)#detectar aquivo frontalface

    objetos = car_cascade.detectMultiScale(gray, 1.6, 6)#detectar aquivo de treinamento de imagens
    print(objetos)
    for (x,y,w,h) in objetos:#pegar coordenadas
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)#ajutar retangulo

        imfImportant = gray[y:y+h, x:x+w]#recorta parte importante
        cv.imshow("Interesse", imfImportant)#imprime parte importante
        
        cv.imwrite("recorte/video" +str(contador) +".jpg", imfImportant)#armazenar recorte do video
        contador += 1 #adicionar numero ao contador para armazenar os nomes

    cv.imshow('Analise', frame)#imprime a imagem da camera

    #transforma em cinza
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("cinza", gray)#mostra a imagem

    #altera as cores de matriz, saturação e valor
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("HSV", hsv)#mostra a imagem

    #deixa embaçado
    blur = cv.GaussianBlur(gray, (7,7), 0)#embaça um pouco a imagem
    cv.imshow("Blur", blur)#mostra a imagem

    #binarização
    adaptativo = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 5)#adapta a imagem para ficar em preto e branco
    cv.imshow("Binário", adaptativo)#mostra a imagem

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # converte a imagem original para o formato de cores HSV
    DetectCloseWindow() # chama a função para fechar a aplicação
    cv.imshow("Camera", frame) # abre camera

    for (x, y, w, h) in detect:
        cv.rectangle(frame, (x, y), (y+h, x+w), (0, 0, 255), 2)
        imfImportant = gray[y:y+h, x:x+w]#recorta parte importante
        cv.imshow("Interesse", imfImportant)#imprime parte importante

        # font = cv.FONT_HERSHEY_SCRIPT_COMPLEX 
        # dt = str(datetime.datetime.now()) #detectar data hora
        # frame = cv.putText(frame, dt, (10, 100), font, 1, (155, 155, 155), 1, cv.LINE_8) 

        cv.imwrite("recorte/face" +str(contador) +".jpg", imfImportant)
        contador += 1

    cv.imshow("Camera", frame)

    key = cv.waitKey(60) #A cada 60 loops de 1 minuto será aguardado se for pressionada alguma tecla

    if ret: 
        font = cv.FONT_HERSHEY_SCRIPT_COMPLEX 
        dt = str(datetime.datetime.now()) #detectar data hora
        frame = cv.putText(frame, dt, (10, 100), font, 1, (155, 155, 155), 1, cv.LINE_8) 
        cv.imwrite("log/" + str("Captura"+str(contador)) +".jpg", frame)
        contador += 1
        cv.imshow('frame', frame) 
  
        key = cv.waitKey(1) 
        if key == 27: 
            break


cv.destroyAllWindows()
camera.release()