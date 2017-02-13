#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
import atexit

# Create the MotorHat object
mh = Adafruit_MotorHAT()

def turnOffMotors():
  mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

MOTOR_ID = 1
STEPS_PER_REV = 200
MOTOR_SPEED = 30 # rpm
STEPS = 2
STEP_TYPE = Adafruit_MotorHAT.DOUBLE
#STEP_TYPE = Adafruit_MotorHAT.INTERLEAVE, MICROSTEP, DOUBLE, SINGLE

theStepper = mh.getStepper(STEPS_PER_REV, MOTOR_ID)
theStepper.setSpeed(MOTOR_SPEED)

def clockwise():
  theStepper.step(STEPS, Adafruit_MotorHAT.FORWARD,  STEP_TYPE)

def counterClockwise():
  theStepper.step(STEPS, Adafruit_MotorHAT.BACKWARD, STEP_TYPE)

GPIO.setmode(GPIO.BCM)
B1=17
B2=22
GPIO.setup(B1, GPIO.IN)
GPIO.setup(B2, GPIO.IN)

while True:
  input_1 = GPIO.input(B1)
  input_2 = GPIO.input(B2)
  if (input_1 == 0):
    clockwise()
  if (input_2 == 0):
    counterClockwise()

  if(input_1 and input_2):
    sleep_time = 0.5
  elif(sleep_time > 0.1):
    sleep_time /= 1.3
  time.sleep(sleep_time)
