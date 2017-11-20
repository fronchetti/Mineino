# -*- coding: utf-8 -*-
# Matéria: Computação Física
# Autores: Felipe Fronchetti e Vinicius ribeiro

import serial  # Fonte: https://pythonhosted.org/pyserial/
import serial.tools.list_ports
from serial import SerialException
from pynput.mouse import Button
from pynput.mouse import Controller as ControllerMouse
from pynput.keyboard import Key, Controller

# Para corrigir erros como "DisplayConnectionError" no Linux
# Execute o seguinte comando: "xhost +"
# Desta forma permitimos acesso do nosso código ao X Server (Display)
# Para mais informações e opções, no terminal: man xhost


class Joystick():

    # Inicia a comunicação serial com o Arduino.
    # Se nenhuma porta é passada por parâmetro, o algoritmo
    # tenta encontrar uma disponível no sistema.

    def __init__(self, porta_joystick=None):
        self.joystick = None

        if porta_joystick is not None:
            try:
                self.joystick = serial.Serial(porta_joystick, 9600)
            except serial.SerialException as erro_serial:
                print('[Arduino] Impossível se conectar a porta definida!')
                raise(erro_serial)
        else:
            self.joystick_porta_padrao = '/dev/ttyACM0'

            portas = list(serial.tools.list_ports.comports())
            print('[Arduino] Nenhuma porta definida, tentando encontrar uma...')

            for porta in portas:
                try:
                    self.joystick = serial.Serial(porta[0], 9600)
                    print('[Arduino] Uma porta correspondente foi encontrada!')
                    print(str(porta))
                except serial.SerialException as erro_serial:
                    print(erro_serial)

            if not self.joystick:
                self.joystick = serial.Serial(
                    self.joystick_porta_padrao, 9600)

    # O flush da entrada e da saída tornam a captura
    # dos dados muito mais eficiente.
    def flush(self):
        self.joystick.flushInput()
        self.joystick.flushOutput()

    # Captura as mensagens seriais emitidas e realiza
    # os respectivos comandos no computador.
    def listen(self):
        # Dicionário de comandos
        dicionario = {
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

        teclas_pressionadas = []

        try:
            while True:
                # Recebe o comando do microcontrolador
                comando = self.joystick.readline().strip()

                if comando in dicionario.keys():

                    # Botões:
                    # Quadrado, triângulo, círculo, forquilha, botão do
                    # analógico
                    if 'TRI' in comando:
                        keyboard.press(dicionario['TRI'])
                        keyboard.release(dicionario['TRI'])
                        print('[Joystick] Triângulo')

                    if 'FRK' in comando:
                        keyboard.press(Key.space)
                        keyboard.release(Key.space)
                        print('[Joystick] Forquilha')

                    if 'SQR' in comando:
                        keyboard.press(Key.shift_l)
                        keyboard.release(Key.shift_l)
                        print('[Joystick] Quadrado')

                    if 'CIR' in comando:
                        keyboard.press(dicionario['CIR'])
                        keyboard.release(dicionario['CIR'])
                        print('[Joystick] Circulo')

                    if 'STR' in comando:
                        mouse.scroll(0, -1)
                        print('[Joystick] Start')

                    if 'SLC' in comando:
                        mouse.scroll(0, 1)
                        print('[Joystick] Select')

                    if 'ANBT' in comando:
                        mouse.click(Button.left)
                        print('[Joystick] Analógico Direcional (Botão)')

                    # Análógicos:
                    # Cima, baixo, esquerda, direita
                    if 'ANU' in comando:
                        teclas_pressionadas.append(dicionario['ANU'])
                        keyboard.press(dicionario['ANU'])
                        print('[Joystick] Analógico Direcional (Frente)')

                    if 'AND' in comando:
                        teclas_pressionadas.append(dicionario['AND'])
                        keyboard.press(dicionario['AND'])
                        print('[Joystick] Analógico Direcional (Trás)')

                    if 'ANL' in comando:
                        teclas_pressionadas.append(dicionario['ANL'])
                        keyboard.press(dicionario['ANL'])
                        print('[Joystick] Analógico Direcional (Esquerda)')

                    if 'ANR' in comando:
                        teclas_pressionadas.append(dicionario['ANR'])
                        keyboard.press(dicionario['ANR'])
                        print('[Joystick] Analógico Direcional (Direita)')

                    if 'ANC' in comando and len(teclas_pressionadas) > 0:
                        for tecla in teclas_pressionadas:
                            keyboard.release(tecla)
                        teclas_pressionadas = []

                    self.flush()

        except KeyboardInterrupt:
            print('\n[Joystick] Erro encontrado, tente novamente.')

keyboard = Controller()
mouse = ControllerMouse()
joystick = Joystick()
joystick.listen()
