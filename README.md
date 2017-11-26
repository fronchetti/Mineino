# Mineino
Play Minecraft using an Arduino and Artificial Intelligence :roller_coaster:

In this project, we simulate keyboard keys and mouse interactions in our operating system to play Minecraft. The keyboard keys are responsible for moving our player, and interacting with the blocks world. It is done using instructions from an joystick, while the mouse is simulated using a face recognition system, used to move the player's camera. We simulate the mouse and the keyboard using Python, so, if you want to use our code in another game or experiment, it's easily possible to change our code.

## Requirements:
+ 1 x Arduino UNO
+ 1 x Joystick Shield (Funduino)

## Dependencies:
Make sure you have installed all the dependencies below:
+ Python 2.7 [[Website](https://www.python.org/)]
+ Pynput [[Website](https://pypi.python.org/pypi/pynput)]
+ Pyserial [[Website](https://pypi.python.org/pypi/pyserial)]
+ OpenCV [[Website](https://opencv.org/)]
+ Arduino IDE [[Website](https://www.arduino.cc/en/main/software)]

## How to use it:
+ Turn on and compile the [sketch.ino](https://github.com/fronchetti/Mineino/blob/master/sketch/sketch.ino) code on your Arduino
+ Open your Minecraft
+ Execute [arduino.py](https://github.com/fronchetti/Mineino/blob/master/arduino.py) and [webcam.py](https://github.com/fronchetti/Mineino/blob/master/webcam.py)
+ Enjoy your game!

> NOTE: We've been testing this code on Ubuntu 16.04, feel free to open an issue if you can not use it on your operating system! External contributions are also well received, don't be shy.
