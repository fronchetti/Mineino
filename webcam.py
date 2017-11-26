# -*- coding: utf-8 -*-
# Authors: Felipe Fronchetti and Vinicius ribeiro
# Source code:
# https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/

import cv2
import sys
from time import sleep
from pynput.mouse import Button
from pynput.mouse import Controller as ControllerMouse

mouse = ControllerMouse()

cascade_xml = "haarcascade_xmlface_default.xml"
cascade = cv2.CascadeClassifier(cascade_xml)
video_capture = cv2.VideoCapture(0)

while True:
    if not video_capture.isOpened():
        print('We\'re not able to open your webcam :(!')
        pass

    # Capture the frames
    ret, frame = video_capture.read()

    # Converts image capture to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Recognizes the face
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)  # Size of each face recognized
    )

    height, width, channels = frame.shape

    #  Draw lines in the image to better guide the player
    cv2.line(frame, (width / 2 - 50, height / 2),
             (width / 2 + 50, height / 2), (255, 255, 255), 2)
    cv2.line(frame, (width / 2, height / 2 + 50),
             (width / 2, height / 2 - 50), (255, 255, 255), 2)

    for (x, y, w, h) in faces:
        # Draw a rectangle around each face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Based on face position, moves the mouse
        # Up and down
        if y > 180:
            mouse.move(0, 50)
        if y < 90:
            mouse.move(0, -50)
        # Left and right
        if x > 250:
            mouse.move(80, 0)
        if x < 180:
            mouse.move(-80, 0)

    # Show the video image in a window
    cv2.imshow('Video', frame)

    # If Q is pressed, stops the execution
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Video', frame)

# Saída do código
video_capture.release()
cv2.destroyAllWindows()
