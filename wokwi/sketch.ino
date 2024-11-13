#include<WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Wokwi-GUEST";
const char* pass = "";
const char* identificador = 'placa_1'

void setup() {

  // Serial.begin(115200);

  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    // Serial.println(".");
  }
  // Serial.println("WiFi Connected!");
  // Serial.println(WiFi.localIP());

  pinMode(32, INPUT);
  pinMode(2, OUTPUT);
}

void loop() {
  int value = analogRead(32);
  int intensity = map(value, 0, 4098, 0, 255);
  analogWrite(2, intensity);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    String url = "https://large-pets-work.loca.lt/api/salvar-dados?value=" + String(intensity) + "&identificador=" + identificador;
    http.begin(url);
    http.GET();
    // int httpResponseCode = http.GET();

    // if (httpResponseCode > 0) {
    //   String payload = http.getString();
    //   Serial.print("Response: ");
    //   Serial.println(payload);
    // } else {
    //   Serial.print("Error: ");
    //   Serial.println(httpResponseCode);
    // }

    http.end();
  } else {
    // Serial.println("WiFi disconnected");
  }

  // Serial.println(intensity);
  delay(200);
}
