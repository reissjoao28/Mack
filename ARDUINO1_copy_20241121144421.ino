#include <SoftwareSerial.h>
SoftwareSerial bluetooth(10, 11); // RX e TX do módulo Bluetooth

// Pinos do Arduino
const int pirPin = 9;        // Pino conectado ao OUT do sensor PIR
const int buzzerPin = 8;     // Pino conectado ao buzzer
const int mc38Pin = 3;       // Pino conectado ao sensor MC38

unsigned long lastTriggerTime = 0;  // Para controlar o tempo entre detecções do PIR
const unsigned long debounceTime = 5000;  // Tempo mínimo entre alertas (5 segundos)

void setup() {
  pinMode(pirPin, INPUT);    // Configura o PIR como entrada
  pinMode(mc38Pin, INPUT_PULLUP); // Configura o MC38 como entrada com pull-up interno
  pinMode(buzzerPin, OUTPUT); // Configura o buzzer como saída

  Serial.begin(9600);        // Inicializa a comunicação serial para debug
  bluetooth.begin(9600);     // Inicializa a comunicação Bluetooth
}

void loop() {
  int pirState = digitalRead(pirPin);  // Lê o estado do PIR
  int mc38State = digitalRead(mc38Pin); // Lê o estado do MC38
  unsigned long currentTime = millis();

  // Verifica se o PIR detectou movimento e se o tempo mínimo passou
  if (pirState == HIGH && (currentTime - lastTriggerTime > debounceTime) && mc38State == HIGH) {
    bluetooth.print("ATIVAR");        // Envia o comando "ATIVAR" para o App Inventor
    Serial.println("Movimento detectado! Porta ou janela aberta!");
    digitalWrite(buzzerPin, HIGH);   // Ativa o buzzer
    delay(500);
    digitalWrite(buzzerPin, LOW);    // Desativa o buzzer
    lastTriggerTime = currentTime;  // Atualiza o último tempo de ativação
  }
  
  delay(100);  // Pequena pausa para estabilidade
}
