#include <Wire.h>

#define I2C_ADDR 9

int i = 0;
char dataToSend[] = "255,128,64";

void setup() {
  Wire.begin();
}

void loop() {
  Wire.beginTransmission(I2C_ADDR);
  Wire.write(dataToSend[i]);
  Wire.endTransmission();

  if (dataToSend[i] == '\0') {
    Wire.requestFrom(I2C_ADDR, 1);
    i = -1;
  }

  i++;

  delay(15);
}
