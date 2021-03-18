#include <Arduino.h>
#include <Wire.h>

#define addr 0x23

byte buffer[2];

void sensor_init();
double sensor_read();

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
  sensor_init();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  double val = sensor_read();
  Serial.println(val);
//  Serial.println(" lx");
  delay(10);
}

void sensor_init()
{
    Wire.beginTransmission(addr);
    Wire.write(0x10);
    Wire.endTransmission();
    delay(30);
}

double sensor_read()
{
    double value; 
    Wire.beginTransmission(addr);
    Wire.requestFrom(addr, 2);
    while(Wire.available())
    {
        buffer[0] = Wire.read();
        delay(50);
        buffer[1] = Wire.read();
    }
    Wire.endTransmission();
    value = (buffer[0] << 8 | buffer[1]) / 1.2;
    return value;
}