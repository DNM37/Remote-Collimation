#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

void setup() {
  Serial.begin(9600);
  servo1.attach(9);  // Attach servo1 to pin 9
  servo2.attach(10); // Attach servo2 to pin 10
  servo3.attach(11); // Attach servo3 to pin 11
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    switch (command) {
      case 'A':
        rotateServo(servo1, 30); // Rotate servo1 30 degrees clockwise
        break;
      case 'B':
        rotateServo(servo1, -30); // Rotate servo1 30 degrees counterclockwise
        break;
      case 'C':
        rotateServo(servo2, 30); // Rotate servo2 30 degrees clockwise
        break;
      case 'D':
        rotateServo(servo2, -30); // Rotate servo2 30 degrees counterclockwise
        break;
      case 'E':
        rotateServo(servo3, 30); // Rotate servo3 30 degrees clockwise
        break;
      case 'F':
        rotateServo(servo3, -30); // Rotate servo3 30 degrees counterclockwise
        break;
      case 'S':
        stopServos(); // Stop all servos
        break;
      default:
        break;
    }
  }
}

void rotateServo(Servo& servo, int degrees) {
  int currentPos = servo.read();
  int targetPos = currentPos + degrees;

  // Limit target position within the valid range (0 to 180 degrees)
  targetPos = constrain(targetPos, 0, 180);

  servo.write(targetPos);
  delay(5);  // Reduce delay for smoother continuous movement
}

void stopServos() {
  servo1.write(servo1.read()); // Stop servo1
  servo2.write(servo2.read()); // Stop servo2
  servo3.write(servo3.read()); // Stop servo3
}



/*
#include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9); // Attach the servo to pin 9
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    switch (command) {
      case 'F':
        rotateServo(30); // Rotate 10 degrees clockwise
        break;
      case 'B':
        rotateServo(-30);  // Rotate 10 degrees counterclockwise
        break;
      case 'S':
        stopServo(); // Stop the movement
        break;
      default:
        break;
    }
  }
}

void rotateServo(int degrees) {
  int currentPos = myServo.read();
  int targetPos = currentPos + degrees;

  // Limit target position within the valid range (0 to 180 degrees)
  targetPos = constrain(targetPos, 0, 180);

  myServo.write(targetPos);
  delay(5);  // Reduce delay for smoother continuous movement
}

void stopServo() {
  myServo.write(myServo.read()); // Stop the servo by writing its current position
}


/*
 * #include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9); // Attach the servo to pin 9
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    switch (command) {
      case 'F':
        rotateServo(10); // Rotate 10 degrees clockwise
        break;
      case 'B':
        rotateServo(-10);  // Rotate 10 degrees counterclockwise
        break;
      default:
        break;
    }
  }
}

void rotateServo(int degrees) {
  int currentPos = myServo.read();
  int targetPos = currentPos + degrees;

  // Limit target position within the valid range (0 to 180 degrees)
  targetPos = constrain(targetPos, 0, 180);

  myServo.write(targetPos);
  delay(500);  // Allow time for the servo to reach the target position
}
 * 
 */
