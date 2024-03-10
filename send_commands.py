'''

import serial
import time

arduino_port = "COM3"  # Update this with the correct port for your Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

def ccw():
    ser.write(b'F1')

def cw():
    ser.write(b'B1')  # Rotate servo 10 degrees counterclockwise

def on_exit():
    ser.close()

'''

import serial
import time

arduino_port = "COM3"  # Update this with the correct port for your Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

#commands for servo1
def ccw1():
    ser.write(b'A')

def cw1():
    ser.write(b'B')  # Rotate servo 10 degrees counterclockwise

#commands for servo2
def ccw2():
    ser.write(b'C')

def cw2():
    ser.write(b'D')  # Rotate servo 10 degrees counterclockwise


#commands for servo3
def ccw3():
    ser.write(b'E')

def cw3():
    ser.write(b'F')  # Rotate servo 10 degrees counterclockwise


#closing the serial port
def on_exit():
    ser.close()

