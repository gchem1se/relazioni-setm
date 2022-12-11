/* SCRIPT SCHEMA MODIFICATO */

const int pin = A3;
const int Vcc = 5; // alimentazione USB 2.0
const int Nbit = 10; // bit ADC
const int S = 0.01; // da: Vout = 10mV * T_K
const long R2 = 68610; 
const long R3 = 32570;

void setup() {
  pinMode(pin, INPUT);
  analogReference(INTERNAL); // set riferimento a 1.1V
  Serial.begin(9600); // baud rate
}

void serialEvent() { // gestito via interrupt
  int Dout = Serial.read(); // valore sensore, da 0 a 1023
  float T_K = Dout * Vcc / pow(2, Nbit) * 1/S * (1 + R2/R3);

  Serial.print("Valore sensore: ");
  Serial.println(Dout);
  Serial.print("Valore temperatura in Kelvin: ");
  Serial.println(T_K);
  Serial.print("Valore temperatura in Celsius: ");
  Serial.println(T_K - 273.15);
  Serial.println("######");
}

void loop() {
  ;
}
