# Mineino
Play Minecraft using an Arduino and Artificial Intelligence :roller_coaster:

In this project, we simulate keyboard keys and mouse interactions in our operating system to play Minecraft. The keyboard keys are responsible for moving our player, and interacting with the block's world. It is done using instructions from an Arduino, while the mouse is simulated using a face recognition system, to move the the player camera. We simulate the mouse and keyboard using two libraries, so, if you want to use our code in another game or experiment, it's easily possible to change our code.

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
+ Compile the [sketch.ino](https://github.com/fronchetti/Mineino/blob/master/sketch/sketch.ino) code on your Arduino
+ Open your Minecraft
+ Execute [arduino.py](https://github.com/fronchetti/Mineino/blob/master/arduino.py) and [webcam.py](https://github.com/fronchetti/Mineino/blob/master/webcam.py)
+ Enjoy your game!
