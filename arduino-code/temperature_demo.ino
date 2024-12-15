#include "Adafruit_Sensor.h"
#include "Adafruit_AM2320.h"

Adafruit_AM2320 am2320 = Adafruit_AM2320();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  am2320.begin();
}

void loop() {
  float temperature = am2320.readTemperature();
  float humidity = am2320.readHumidity();

  outputTemperature(temperature);
  /*
  Serial.println("Temperature: "+String(temperature));
  Serial.println("Humidity: "+String(humidity));
  */
  delay(3000);
}
void outputTemperature(float t) {
  /*
  Outputs the temperature in the format expected by the python heater controller.
  :param t: The temperature value
  */
  Serial.print('b'+String(t)+'\\');
}
