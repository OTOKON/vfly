#include <Wire.h>

#define I2C_ADDR 9

volatile char receivedData;
String data = "";

void setup() {
  Serial.begin(9600);

  Wire.begin(I2C_ADDR);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {

}

void receiveEvent(int bytes)
{
  receivedData = Wire.read();

  if (receivedData != '\0')
    data += receivedData;
}

void requestEvent()
{
  splitData(data);
  Wire.write(0xFF);
}

void splitData(String strToParsed)
{
  int i = 0;
  String splittedData = "";

  while (strToParsed[i] != ',') {
    splittedData += strToParsed[i];
    i++;
  }

  data = "";
}
