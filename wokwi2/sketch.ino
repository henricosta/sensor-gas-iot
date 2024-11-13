#include<WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Wokwi-GUEST";
const char* pass = "";

void setup() {
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
  }
  pinMode(32, INPUT);
}

void loop() {
  int value = analogRead(32);
  int intensity = map(value, 0, 4098, 0, 255);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    String url = "https://cute-badgers-fail.loca.lt/api/salvar-dados?identificador=placa_1&value=" + String(intensity);
    http.begin(url);
    http.GET();
    http.end();
  }

  delay(200);
}
