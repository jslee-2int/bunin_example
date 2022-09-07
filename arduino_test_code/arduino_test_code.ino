long randNumber;
String list[6];

void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(38400);
  while (!Serial);
  Serial.println("E0 E1 F2 F2 A3 A3 B4 B4 C5 C5 D6 D6");
}

void loop() {
  if (Serial.available())
  {
    int state = Serial.parseInt();
    if (state == 1)
      {
      digitalWrite(13, HIGH);
      for (int i = 0; i <= 6; i++){
        randNumber = random(2000, 50000);
        String stringOne = String(randNumber, HEX);
        if (stringOne.length() == 3){
          stringOne = "0" + stringOne;    
        }
        String str1 = stringOne.substring(0,2);
        String str2 = stringOne.substring(2,4);
        list[i] = str1 + " " + str2;
      }
      Serial.println(list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]+" "+list[5]);
      }
    if (state == 2)
      {
      digitalWrite(13, LOW);
      for (int i = 0; i <= 6; i++){
        randNumber = random(300, 50000);
        String stringOne = String(randNumber, HEX);
        if (stringOne.length() == 3){
          stringOne = "0" + stringOne;    
        }
        String str1 = stringOne.substring(0,2);
        String str2 = stringOne.substring(2,4);
        list[i] = str1 + " " + str2;
      }
      Serial.println(list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]+" "+list[5]);
      }
  }
}
