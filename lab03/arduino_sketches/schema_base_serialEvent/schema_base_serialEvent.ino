/* SCRIPT SCHEMA BASE*/

const int pin = A3;
const int Vcc = 5; // alimentazione USB 2.0
const int Nbit = 10; // bit ADC
const int S = 0.01; // da: Vout = 10mV * T_K

void setup() {
  pinMode(A3, INPUT);
  Serial.begin(9600); // baud rate
}

void serialEvent() { // gestito via interrupt
  int Dout = Serial.read(); // valore sensore, da 0 a 1023
  float T_K = Dout * Vcc / pow(2, Nbit) * 1/S; 

  Serial.print("Valore sensore: ");
  Serial.println(Dout);
  Serial.print("Temperatura in Kelvin: ");
  Serial.println(T_K);
  Serial.print("Temperatura in Celsius: ");
  Serial.print(T_K - 273.15);
  Serial.println("######");
}

void loop() {
  ;
}
