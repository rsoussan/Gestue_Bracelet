/*
 Sends acceleromter data from arduino using the xbee device.  Triggers send when bracelet is 
 "jerked" (accelerometer values are large enough).  Referenced from: 
 http://www.arduino.cc/en/Tutorial/ADXL3xx
 analog 0: Vin
 analog 1: 3vo
 analog 2: ground
 analog 3: z-axis
 analog 4: y-axis
 analog 5: x-axis
 */

#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);
// these constants describe the pins. They won't change:
const int xpin = A5; // x-axis of the accelerometer
const int ypin = A4; // y-axis
const int zpin = A3; // z-axis 

int xval;
int yval;
int zval;
int sum_val = 1000; // start in range
int jerk_max = 1400;
int jerk_min = 650;
int millisecs = 700;
int num_reads;
int milli_delay = 5;
int waits = 11; // in millidelay units
int num_waits;
int baud_rate = 19200;
void setup()
{
  // initialize the serial communications:
  mySerial.begin(baud_rate);
  num_reads = millisecs/milli_delay;
  num_waits = waits*milli_delay;
}
void loop()
{
  xval = analogRead(xpin);
  yval = analogRead(ypin);
  zval = analogRead(zpin);
  // wait for jerk
   sum_val = xval+yval+zval;
  if (sum_val >  jerk_max || sum_val < jerk_min) {
    // delay after jerk
    for (int i = 0; i < num_waits; i++)
    {
      delay(milli_delay);
    }
    mySerial.println("start");
    // send data
    for (int i = 0; i < num_reads; i++) 
    {
      xval = analogRead(xpin);
      yval = analogRead(ypin);
      zval = analogRead(zpin);
      String out = String(xval) + "\t" + String(yval) + "\t" + String(zval);
      mySerial.println(out);
    }
    mySerial.println("end");
  }
  // delay before next reading:
  delay(milli_delay);
}


