#include <Keyboard.h>

int up_button = 2;
int down_button = 4;
int left_button = 5;
int right_button = 3;
int start_button = 6;
int select_button = 7;
int joystick_button = 8;
int joystick_axis_x = A0;
int joystick_axis_y = A1;
int buttons[] = {up_button, down_button, left_button, right_button, start_button, select_button, joystick_button};


void setup() {
  Serial.begin(9600);
  for (int i; i < 7; i++)
  {
   pinMode(buttons[i], INPUT);
   digitalWrite(buttons[i], HIGH);
  }
}

void loop() {
  /* Botões:
     Os botões recebem valores booleanos, quando pressionados, recebem valor zero. Quando soltos, recebem valor um
     Os botões disponíveis são: cima, baixo, direita, esquerda, start e select.

     Os botões cima e baixo são denotados pela cor amarela. Os botões esquerda e direita são denotados pela cor azul.
     Os botões select e start ficam ao centro do Joystick Shield. Start a direita e select a esquerda.

     Analógico:
     O shield conta com apenas um analógico, com valores mapeados entre zero e mil, variando entre o eixo x e eixo y.
  */

  int up_button_value = digitalRead(up_button);
  int down_button_value = digitalRead(down_button);
  int left_button_value = digitalRead(left_button);
  int right_button_value = digitalRead(right_button);
  int start_button_value = digitalRead(start_button);
  int select_button_value = digitalRead(select_button);
  int joystick_button_value = digitalRead(joystick_button);

  // Triângulo
  if(up_button_value == 0) {
    Serial.print("TRI\n");  
  }
  // Xis
  if(down_button_value == 0) {
    Serial.print("FRK\n");  
  }
  // Quadrado
  if(left_button_value == 0) {
    Serial.print("SQR\n");  
  }
  // Circulo
  if(right_button_value == 0) {
    Serial.print("CIR\n");  
  }
  // Start
  if(start_button_value == 0) {
    Serial.print("STR\n");  
  }
  // Select
  if(select_button_value == 0) {
    Serial.print("SLC\n");  
  }
  // Analógico (Pressionar)
  if(joystick_button_value == 0) {
    Serial.print("ANBT\n");  
  }

  int joystick_axis_x_value = map(analogRead(joystick_axis_x), 0, 1000, -1, 1);
  int joystick_axis_y_value = map(analogRead(joystick_axis_y), 0, 1000, -1, 1);

  // Analógico Direita
  if(joystick_axis_x_value == 1) {
    Serial.print("ANR\n");  
  }

  // Analógico Esquerda
  if(joystick_axis_x_value == -1) {
    Serial.print("ANL\n");  
  }

  // Analógico Cima
  if(joystick_axis_y_value == 1) {
    Serial.print("ANU\n");  
  }

  // Analógico baixo
  if(joystick_axis_y_value == -1) {
    Serial.print("AND\n");  
  }

  if(joystick_axis_y_value == 0 && joystick_axis_x_value == 0) {
    Serial.print("ANC\n");
  }

  delay(100);
 }

