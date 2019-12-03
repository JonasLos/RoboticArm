import time
import math
import Adafruit_BBIO.GPIO as GPIO
import socket
import json

UDP_IP = "192.168.8.1"
UDP_PORT = 2442

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

steps = 0
step = 0
angle = 0
stepPin1 = "P8_7"
dirPin1 = "P8_8"
stepPin2 = "P8_9"
dirPin2 = "P8_10"
stepPin3 = "P8_11"
dirPin3 = "P8_12"
stepPin4 = "P8_15"
dirPin4 = "P8_16"

GPIO.setup(stepPin1, GPIO.OUT)
GPIO.setup(dirPin1, GPIO.OUT)
GPIO.setup(stepPin2, GPIO.OUT)
GPIO.setup(dirPin2, GPIO.OUT)
GPIO.setup(stepPin3, GPIO.OUT)
GPIO.setup(dirPin3, GPIO.OUT)
GPIO.setup(stepPin4, GPIO.OUT)
GPIO.setup(dirPin4, GPIO.OUT)

steps_per_rev = 200
angleMotor1 = 0
angleMotor2 = 0
angleMotor3 = 0 
angleMotor4 = 0 


def moveMotor1(degrees, rpm):
	step = 0
	steps = 0 
	angle = 0 
	wait_time = 60.0/(steps_per_rev*rpm)
	steps = math.fabs(degrees*steps_per_rev/360.0)
	
	if degrees < 0:
		direction = -1
		GPIO.output(dirPin1, GPIO.LOW)
	else:
		direction = 1
		GPIO.output(dirPin1, GPIO.HIGH)
		
	while step < steps:
		
				GPIO.output(stepPin1, GPIO.HIGH)
				time.sleep(wait_time)
				step += 1
				#angle = (angle + (direction *1.8)/32.0) 
				#print(angle)
				angle = (angle + (direction *1.8)/32.0)
				GPIO.output(stepPin1, GPIO.LOW)
	print("Motor 1 Moved")
	angleMotor1 = angle
	print(angleMotor1)
	return(angleMotor1)
				
def moveMotor2(degrees, rpm):
        step = 0
        angle = 0
	steps = 0 

	wait_time = 60.0/(steps_per_rev*rpm)
	steps = math.fabs(degrees*steps_per_rev/360.0)
	
	if degrees < 0:
		direction = -1
		GPIO.output(dirPin2, GPIO.LOW)
	else:
		direction = 1
		GPIO.output(dirPin2, GPIO.HIGH)

	while step < steps:

				GPIO.output(stepPin2, GPIO.HIGH)
				time.sleep(wait_time)
				step += 1
				if (angle <= -120 or angle >= 120):
					if angle <= -120:
						angle = -119.9
					elif angle >= 120:
						angle = 119.9
					break
				angle = (angle + direction/steps_per_rev*360.0) % 360.0
				GPIO.output(stepPin2, GPIO.LOW)
	print("Motor 2 Moved")

def moveMotor3(degrees, rpm):
        step = 0
	angle = 0
	steps = 0 

	wait_time = 60.0/(steps_per_rev*rpm)
	steps = math.fabs(degrees*steps_per_rev/360.0)

	if degrees < 0:
		direction = -1
		GPIO.output(dirPin3, GPIO.LOW)
	else:
		direction = 1
		GPIO.output(dirPin3, GPIO.HIGH)

	while step < steps:

				GPIO.output(stepPin3, GPIO.HIGH)
				time.sleep(wait_time)
				step += 1
				if (angle <= 0 or angle >= 800):
					if angle <= 800:
						angle = 799.9
					elif angle >= 0:
						angle = 0.1
					break
				angle = (angle + direction/steps_per_rev *360.0) % 360.0
				GPIO.output(stepPin3, GPIO.LOW)
	print("Motor 3 Moved")


while True:

	moveMotor1(-45 *32.0 ,5 * 32.0)
	moveMotor2(-90 * 32.0, 5 *32.0) 
	time.sleep(2)
	moveMotor3(750*32.0, 15*32.0)
	moveMotor2(90*32.0, 5*32.0)
	time.sleep(2)
	moveMotor1(45*32.0, 5*32.0)
	moveMotor2(-90 *32.0, 5*32.0)
	moveMotor3(-750 *32.0, 15 *32.0 )
	moveMotor2(90*32.0, 5*32.0)
