#define BIT_PIN 13
#define DATA_PIN 12
String data = "Srujan";

void setup()
{
Serial.begin(9600);
pinMode(DATA_PIN, OUTPUT);
pinMode(BIT_PIN, OUTPUT);
}


void loop() {
 for(int charPos = 0; charPos < data.length(); charPos++){
 char charAtPos = data.charAt(charPos);
 for(int bitPos = 7; bitPos >= 0; bitPos--){
 bool bitValue = bitRead(charAtPos, bitPos);
  Serial.println(bitValue);
  digitalWrite(BIT_PIN, bitValue);
  delay(500);
  digitalWrite(DATA_PIN, HIGH);
  delay(500);
  digitalWrite(DATA_PIN, LOW);

}

Serial.println("");

}
}