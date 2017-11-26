# -*- coding: utf-8 -*-
# Authors: Felipe Fronchetti and Vinicius ribeiro

import serial
import serial.tools.list_ports
from serial import SerialException
from pynput.mouse import Button
from pynput.mouse import Controller as ControllerMouse
from pynput.keyboard import Key, Controller

# If you executed the code, and received an "DisplayConnectionError" on Linux
# Execute the following command: "xhost +"
# This commands allows the code to use the display
# Read more about it on your terminal: man xhost


class Joystick():

    # Starts the communication with Arduino
    # If no port is defined, the method tries to find
    # one available on the system.

    def __init__(self, joystick_port=None):
        self.joystick = None

        if joystick_port is not None:
            try:
                self.joystick = serial.Serial(joystick_port, 9600)
            except serial.SerialException as serial_error:
                print('[Arduino] Impossible to use the defined port!')
                raise(serial_error)
        else:
            print('[Arduino] No port was defined, trying to find a new one...')

            self.joystick_standard_port = '/dev/ttyACM0'

            ports = list(serial.tools.list_ports.comports())

            for port in ports:
                try:
                    self.joystick = serial.Serial(port[0], 9600)
                    print('[Arduino] An Arduino port was find, trying it!')
                except serial.SerialException as serial_error:
                    print(serial_error)

            if not self.joystick:
                self.joystick = serial.Serial(
                    self.joystick_standard_port, 9600)

    # Improves joystick readability
    def flush(self):
        self.joystick.flushInput()
        self.joystick.flushOutput()

    # Listen the instructions from Arduino
    def listen(self):
        commands = {
            # Instruction : Key
            'ANU': 'w',
            'AND': 's',
            'ANL': 'a',
            'ANR': 'd',
            'ANC': None,
            'ANBT': None,
            'SQR': 'd',
            'TRI': 'e',
            'CIR': 'p',
            'FRK': 'v',
            'SLC': None,
            'STR': None
        }

        keystrokes = []

        try:
            while True:
                # Receives instructions from Arduino
                command = self.joystick.readline().strip()

                if command in commands.keys():
                    # We have commands that are pressed only once,
                    # and commands that are pressed until a certain condition.

                    # Buttons (Press and release):
                    # Square, triangle, circle, fork, and analog
                    if 'TRI' in command:
                        keyboard.press(commands['TRI'])
                        keyboard.release(commands['TRI'])
                        print('[Joystick] Triangle')

                    if 'FRK' in command:
                        keyboard.press(Key.space)
                        keyboard.release(Key.space)
                        print('[Joystick] Fork')

                    if 'SQR' in command:
                        keyboard.press(Key.shift_l)
                        keyboard.release(Key.shift_l)
                        print('[Joystick] Square')

                    if 'CIR' in command:
                        keyboard.press(commands['CIR'])
                        keyboard.release(commands['CIR'])
                        print('[Joystick] Circle')

                    if 'STR' in command:
                        mouse.scroll(0, -1)
                        print('[Joystick] Start')

                    if 'SLC' in command:
                        mouse.scroll(0, 1)
                        print('[Joystick] Select')

                    if 'ANBT' in command:
                        mouse.click(Button.left)
                        print('[Joystick] Analog Button')

                    # Analog (Press and hold):
                    # Forward, backward, left and right
                    if 'ANU' in command:
                        keystrokes.append(commands['ANU'])
                        keyboard.press(commands['ANU'])
                        print('[Joystick] Directional Analog (Forward)')

                    if 'AND' in command:
                        keystrokes.append(commands['AND'])
                        keyboard.press(commands['AND'])
                        print('[Joystick] Directional Analog (Backward)')

                    if 'ANL' in command:
                        keystrokes.append(commands['ANL'])
                        keyboard.press(commands['ANL'])
                        print('[Joystick] Directional Analog (Left)')

                    if 'ANR' in command:
                        keystrokes.append(commands['ANR'])
                        keyboard.press(commands['ANR'])
                        print('[Joystick] Directional Analog (Right)')

                    if 'ANC' in command and len(keystrokes) > 0:
                        print('[Joystick] Directional Analog (Center)')
                        print('[System] Removing keystrokes...')
                        for key in keystrokes:
                            keyboard.release(key)
                        keystrokes = []

                    self.flush()

        except KeyboardInterrupt:
            print('\n[Joystick] An keyboard error was found, try again!')

keyboard = Controller()
mouse = ControllerMouse()
joystick = Joystick()
joystick.listen()
