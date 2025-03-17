//Used Arduino and C Code on Thinkercad

//Analog Input Sensor TMP36
int sensorPin = A0;

//Digital Output
int LED = 5;
int motor = 8;
int buzzer = 9;

void setup()
{
  // Analog Input
  pinMode(A0, INPUT);
  
  // Digital Output
  pinMode(LED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(motor, OUTPUT);
}

void loop()
{  
  int sensorValue = analogRead(sensorPin);
  
  float voltage = sensorValue * (5.0 / 1023.0);
  
  float temperature = (voltage - 0.5) * 100.0;
  
  if(temperature < 30.0){
      digitalWrite(buzzer, LOW);
      digitalWrite(motor, LOW);
      digitalWrite(LED, LOW);
    }

    else if(temperature >= 30.0 && temperature < 50.0){
      digitalWrite(buzzer, LOW);
      digitalWrite(motor, HIGH);
      digitalWrite(LED, LOW);
    }

    else{
      digitalWrite(motor, HIGH);
      digitalWrite(buzzer, HIGH);
      digitalWrite(LED, HIGH);
    }
  	
  	delay(1000); //await 1 sec
}