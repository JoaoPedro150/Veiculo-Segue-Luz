#include <Ultrasonic.h>
#include <AFMotor.h>

#define LINE_BREAK '@'

#define pino_trigger 31
#define pino_echo 33

Ultrasonic ultrasonic(pino_trigger, pino_echo);

AF_DCMotor roda_direita(3);
AF_DCMotor roda_esquerda(4);

const int ledMsg = 22;
const int ledUltrassonic = 24;
const int led_modo_seguir = 26;
const int botao = 28;
const int ldr_dir = A14;
const int ldr_esq = A15;

String movimento;
String ultimo_movimento = "F";

const int distMin = 25;
int in_movimento = 0;
int distancia = 0;
int seq = 0;
int seguir_luz = 0;
int diferenca;
int value_ldr_dir;
int value_ldr_esq;

void setup() {
  Serial.begin(9600);
  Serial3.begin(9600);

  pinMode(ledMsg, OUTPUT);
  pinMode(ledUltrassonic, OUTPUT);
  pinMode(led_modo_seguir, OUTPUT);
}

void loop() {
  movimento = ler_bluetooth(); 
  
  if (digitalRead(botao))
    if (seguir_luz) {
      digitalWrite(led_modo_seguir, LOW);
      seguir_luz = 0;
    }
    else {
      digitalWrite(led_modo_seguir, HIGH);
      seguir_luz = 1;
    }
  
  if (movimento == "B")
    move_tras(movimento);
  else if (movimento == "D")
    move_dir(movimento);
  else if (movimento == "E")
    move_esq(movimento);
  else if (movimento == "F")
    move_frente(movimento);
  else if (seq < 5 && (analogRead(ldr_esq) < 800 || analogRead(ldr_dir) < 800) && seguir_luz) {
    
      diferenca = 12 * (analogRead(ldr_esq) - analogRead(ldr_dir)) / 100;
    
      if (diferenca > 10)
        move("S", FORWARD, FORWARD, 210 + diferenca + 10, 220);
      else if (diferenca < -10)
        move("S", FORWARD, FORWARD, 210, (diferenca * -1) + 220);
      else
        move("S", FORWARD, FORWARD, 210, 220);
    }
  else if (ultimo_movimento == "S")
      parar();
        
  if (ultrasonic.read() < distMin) {
    seq += 1;
    
    if (seq > 5) {
    digitalWrite(ledUltrassonic, HIGH);
    
      if (ultimo_movimento == "F" || ultimo_movimento == "S") {
        parar();
        return 0;
      }
    }
  }
  else {
    seq = 0;
    digitalWrite(ledUltrassonic, LOW);
  }
    
  digitalWrite(ledMsg, LOW);
}

String ler_bluetooth() {
   String mensagem;

   while(Serial3.available()){

     digitalWrite(ledMsg, HIGH);

     char c = Serial3.read();

     if(c == LINE_BREAK) break;

     mensagem += c;

   }
  
   return mensagem;
}

void move_dir(String movimento) {
  virar(movimento, BACKWARD, FORWARD, 200, 255);
}

void move_esq(String movimento) {
  virar(movimento, FORWARD, BACKWARD, 255, 200);
}

void virar(String movimento, int mov_dir, int mov_esq, int speed_dir, int speed_esq) {
  if (in_movimento) {
    roda_direita.setSpeed(speed_dir);
    roda_esquerda.setSpeed(speed_esq);
  }
  else
    move(movimento, mov_dir, mov_esq, 210, 210);
}

void move_frente(String movimento) {
  move(movimento, FORWARD, FORWARD, 210, 240);
}

void move_tras(String movimento) {
  if (in_movimento) 
    parar();

  else 
    move(movimento, BACKWARD, BACKWARD, 210, 210);
}

void move(String movimento, int mov_dir, int mov_esq, int speed_dir, int speed_esq) {
    roda_esquerda.setSpeed(speed_esq);
    roda_esquerda.run(mov_esq);

    roda_direita.setSpeed(speed_dir);
    roda_direita.run(mov_dir);
    
    in_movimento = 1;
    ultimo_movimento = movimento;
}

void parar() {
    roda_direita.run(RELEASE);
    roda_esquerda.run(RELEASE);
    
    in_movimento = 0;
}