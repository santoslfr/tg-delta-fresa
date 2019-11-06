#include "PS2Mouse.h"

///////////////////////////////////////////////////////////////////////////////////////////
// comunicação serial arduino-raspberry pi para recebimento de comandados de acionamento //
// dos motores e envio do status dos sensores                                            //
///////////////////////////////////////////////////////////////////////////////////////////

//configuração dos mouses

// definição dos pinos aos quais estão ligados as linas de clock e data dos mouses

// mouse A2
#define DATA_PIN_A2 11
#define CLOCK_PIN_A2 10
int bd_A2 = 0; //status do botão direito ( sensor de fim de curso do eixo z)

// mouse B2
#define DATA_PIN_B2 7
#define CLOCK_PIN_B2 6
int bd_B2 = 0; //status do botão direito ( sensor de fim de curso do eixo z)

// mouse C2
#define DATA_PIN_C2 3
#define CLOCK_PIN_C2 2
int bd_C2 = 0; //status do botão direito ( sensor de fim de curso do eixo z)

PS2Mouse mouse_A2(CLOCK_PIN_A2, DATA_PIN_A2);// criação de objeto da classe PS2Mouse
PS2Mouse mouse_B2(CLOCK_PIN_B2, DATA_PIN_B2);
PS2Mouse mouse_C2(CLOCK_PIN_C2, DATA_PIN_C2);

/////////////////////////////////////////////////////////////////////////////////////////

//configuração dos motores

//pinos digitais atribuidos as entradas "direção" e "passo" do drive DRV 8825 de cada motor

#define STEP_A A5 //12
#define DIR_A A4 //13
#define STEP_B A3 //8
#define DIR_B A2 //9
#define STEP_C A1 //4
#define DIR_C A0 //5

//instrução de direção e semtido de passo recebida via comunicação serial

int MA_S;
int MA_D;
int MB_S;
int MB_D;
int MC_S;
int MC_D;

/////////////////////////////////////////////////////////////////////////////////////////

byte incomingByte;// variavel que registra os dados recebidos via comunicação serial
int temp; // espera de dados

/////////////////////////////////////////////////////////////////////////////////////////

void setup() {
  
  Serial.begin(9600); // inicia comunicação serial
 
  mouse_A2.initialize(); // Inicio da comunicação entre microcontrolador e mouse
  mouse_B2.initialize();
  mouse_C2.initialize();  
}

/////////////////////////////////////////////////////////////////////////////////////////

void ler_mouse() {
  
  MouseData dataA2 = mouse_A2.readData(); // leitura dos dados dos mouses
  MouseData dataB2 = mouse_B2.readData();
  MouseData dataC2 = mouse_C2.readData();
  
  // menssagem com os dados dos mouses
      
  Serial.print(dataA2.position.x); // deslocamento no eixo x desde a ultima leitura
  Serial.print(';');               // caracter de divisão entre os dados
  Serial.print(dataA2.position.y); // deslocamento no eixo y desde a ultima leitura
  Serial.print(';');  
  Serial.print(dataA2.status);     // status dos botões do mouse
  Serial.print(';');  
  Serial.print(dataB2.position.x);
  Serial.print(';');  
  Serial.print(dataB2.position.y);
  Serial.print(';');
  Serial.print(dataB2.status);
  Serial.print(';');  
  Serial.print(dataC2.position.x);
  Serial.print(';');  
  Serial.print(dataC2.position.y);
  Serial.print(';');  
  Serial.print(dataC2.status);
  Serial.print('\r');
  
  incomingByte = B00000000;
  
}

/////////////////////////////////////////////////////////////////////////////////////////

void acionar_motor() {

//do{

temp = Serial.available();

while (temp == 0){

temp = Serial.available();
 //Serial.flush();
}

temp = 0;
incomingByte = Serial.read();

if(incomingByte != 0){

// MA_S = 1; relizar passo
// MA_S = 0; não realizar passo
// MA_D = 1; rotação sentido anti-horário
// MA_D = 0; rotação sentido horário

  MA_S = incomingByte & B00000001;
  MA_D = (incomingByte >> 1) & B00000001;
  MB_S = (incomingByte >> 2) & B00000001;
  MB_D = (incomingByte >> 3) & B00000001;
  MC_S = (incomingByte >> 4) & B00000001;
  MC_D = (incomingByte >> 5) & B00000001;

  digitalWrite(DIR_A,1*(1 - MA_D));
  digitalWrite(STEP_A,LOW);
  delayMicroseconds(100);
  digitalWrite(STEP_A, MA_S);
  
  digitalWrite(DIR_B,1*(1 - MB_D));
  digitalWrite(STEP_B,LOW);
  delayMicroseconds(100); 
  digitalWrite(STEP_B,MB_S);
  
  digitalWrite(DIR_C,1*(1 - MC_D));
  digitalWrite(STEP_C,LOW);
  delayMicroseconds(100); 
  digitalWrite(STEP_C,MC_S);

  incomingByte = B00000000; // limpa a variavel

  Serial.write("e"); // avisa que está pronto para receber o proximo passo
  //incomingByte = Serial.read();
}

//}while(incomingByte!=B11000000); // B11000000 é o código ASCII de "À" : sinaliza o fim do envio de passos

}

/////////////////////////////////////////////////////////////////////////////////////////

void reset(){

// calibração inicial da estrutura

do{

// le o status do sensor de fim de curso

    MouseData data2 = mouse_A2.readData();
    MouseData data4 = mouse_B2.readData();
    MouseData data6 = mouse_C2.readData();

//bd_A2 = 0; botão não pressionado
//bd_A2 = 0; botão pressionado
    
    bd_A2 = data2.status;
    bd_A2 = bd_A2 >> 2; // desloca todos os bits 3 posições pra a direita
    bd_A2 = bd_A2 & B00000001; // filtra somente o primeiro bit : status do botão direito

    bd_B2 = data4.status;
    bd_B2 = bd_B2 >> 2; // desloca todos os bits 3 posições pra a direita
    bd_B2 = bd_B2 & B00000001; // filtra somente o primeiro bit : status do botão direito

    bd_C2 = data6.status;
    bd_C2 = bd_C2 >> 2; // desloca todos os bits 3 posições pra a direita
    bd_C2 = bd_C2 & B00000001; // filtra somente o primeiro bit : status do botão direito

//DIR_X = 0; rotação sentido anti-horário
//DIR_X = 1; rotação sentido horário

    digitalWrite(DIR_A,LOW);
    digitalWrite(STEP_A,LOW);
    delayMicroseconds(100);
    digitalWrite(STEP_A,(1 - bd_A2));

    digitalWrite(DIR_B,LOW);
    digitalWrite(STEP_B,LOW);
    delayMicroseconds(100);
    digitalWrite(STEP_B,(1 - bd_B2));

    digitalWrite(DIR_C,LOW);
    digitalWrite(STEP_C,LOW);
    delayMicroseconds(100);
    digitalWrite(STEP_C,(1 - bd_C2));
    
}while(bd_A2*bd_B2*bd_C2 != 1);

 //do{
 Serial.write("p"); // informa o fim da calibração
 incomingByte = B00000000;
 //if (Serial.available() > 0){
 //incomingByte = Serial.read();
 //Serial.flush();
 //}
 //}while(incomingByte != B01110000); // B01110000 é o código ASCII de "p" 
}

/////////////////////////////////////////////////////////////////////////////////////////

void loop() {

if (Serial.available() > 0) {

 incomingByte = Serial.read();
 Serial.flush();
 
 }

switch (incomingByte){

case B01110010: // B01110010 é o código ASCII de "r" : requisição de reset da posição inicial do robô
    reset();    
    break;
case B01100001: // B01100001 é o código ASCII de "a" : requisição de acionamento do motor
    acionar_motor();
    break;
case B01101100: // 01101100 é o código ASCII de "l" : requisição de leitura dos dados dos mouse
    ler_mouse();
    break;
}

}
