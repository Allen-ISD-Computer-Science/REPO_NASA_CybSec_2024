#define BIT_PIN 3
#define DATA_PIN 2

void setup()
{
  
  pinMode(DATA_PIN, OUTPUT);
  pinMode(BIT_PIN, OUTPUT);
  Serial.begin(9600);
  
}

void loop(){
  if(Serial.available() > 0){
    String recievedString = "";
    
    while(Serial.available() > 0){
      recievedString += Serial.readStringUntil('\n');
      
    }
    
    for(int charPos = 0; charPos < recievedString.length(); charPos++){
        char charAtPos = recievedString.charAt(charPos);
        for(int bitPos = 7; bitPos >= 0; bitPos--){
          bool bitValue = bitRead(charAtPos, bitPos);
          Serial.println(bitValue);
          digitalWrite(BIT_PIN, bitValue);
          delay(10);
          digitalWrite(DATA_PIN, HIGH);
          delay(10);
          digitalWrite(DATA_PIN, LOW);

      }

    Serial.println("");

        }
  }
}