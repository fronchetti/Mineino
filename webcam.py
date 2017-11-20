# -*- coding: utf-8 -*-
# Matéria: Computação Física
# Autores: Felipe Fronchetti e Vinicius ribeiro
# Tutorial:
# https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/

import cv2
import sys
from time import sleep
from pynput.mouse import Button
from pynput.mouse import Controller as ControllerMouse

# Instância do mouse virtual
mouse = ControllerMouse()

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # O código para de funcionar caso haja problemas com a câmera
    if not video_capture.isOpened():
        print('Não foi possível abrir a câmera.')
        pass

    # Captura o vídeo frame por frame
    ret, frame = video_capture.read()

    # Converte a captura de imagem pra tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta as faces na imagem
    # minSize define o tamanho da face que ele vai capturar
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)  # Tamanho da cabeça (Felipe Size)
    )

    height, width, channels = frame.shape

    # Desenhamos linhas na imagem para melhor orientar o usuário
    cv2.line(frame, (width / 2 - 50, height / 2),
             (width / 2 + 50, height / 2), (255, 255, 255), 2)
    cv2.line(frame, (width / 2, height / 2 + 50),
             (width / 2, height / 2 - 50), (255, 255, 255), 2)

    for (x, y, w, h) in faces:
        # Desenha um retângulo em torno de cada face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Com base na posição da face, move o mouse no sistema
        if y > 180:
            mouse.move(0, 50)
        if y < 90:
            mouse.move(0, -50)

        if x > 250:
            mouse.move(80, 0)
        if x < 180:
            mouse.move(-80, 0)

    # Apresenta o resultado em uma janela de saída
    cv2.imshow('Video', frame)

    # Se o botão Q for pressionado, cancela a execução
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Video', frame)

# Saída do código
video_capture.release()
cv2.destroyAllWindows()
