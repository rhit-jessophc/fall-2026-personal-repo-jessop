String inputString = "";
bool isStringComplete = false;
bool weFlashingNow = false;
int flashPeriod = 0;
int numFlashes = 0;

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    // handle terminal command directory
  if (isStringComplete) {
    if (inputString.equals("LED ON")) {
        handleLedOn();
    } else if (inputString.equals("LED OFF")) {
      handleLedOff();
    } else if {(inputString.startsWith("FLASH"))
        handleFlash(inputString.substring(5));
    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
    }
    // reset terminal input for next command 
    inputString = "";
    isStringComplete = false;
}
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}

void handleLedOn() {
    digitalWrite(13, HIGH);
      Serial.println("The LED is now on!");
}

void handleLedOff() {
    digitalWrite(13, LOW);
      Serial.println("The LED is now off!");
}

void handleFlash(String params) {
    //remove spaces in command 
    params.trim();
    int spaceIndex = params.indexOf(' ')
    
    // if there are no spaces, print error message to terminal 
      if (spaceIndex == -1) {
    Serial.print("Unknown command --> ");
    Serial.println(inputString);
    return;
    }
    
    numFlashes = params.substring(0, spaceIndex).toInt();
    flashPeriod = params.substring(spaceIndex + 1).toInt();

    Serial.println(string("Flashing ") + numFlashes + " " + flashPeriod);

    while (numFlashes > 0) {     

        digitalWrite(13, HIGH);
        delay(flashPeriod/2);
        digitalWrite(13, LOW);
        delay(flashPeriod/2);
        numFlashes = numFlashes - 1;
    }

}


