#define CLOCK_LIGHT A1
#define DATA_LIGHT A0

short lightAmt = 55;

bool dataRead = false;


char currChar = 0;

short currCharPos = 7;


void setup()

{


  Serial.begin(9600);

}


void loop()

{



  short clockVal = analogRead(CLOCK_LIGHT);

  bool clockBool = clockVal > lightAmt;

   

  short dataVal = analogRead(DATA_LIGHT);

  bool dataBool = dataVal > lightAmt;

  

  

  if(clockBool) {

    

    if(!dataRead){

    

    dataRead = true;

      

      currChar = currChar | (dataBool << currCharPos);

      currCharPos--;

    

    } 

    

    if (currCharPos == -1)

    {

    

    Serial.print(currChar);

      currChar = 0;

      currCharPos = 7;

    

    }

    

  } else {

  

  dataRead = false;

  

  }

  

}