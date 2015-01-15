from RPIO import PWM
import time
import math

class ServoController:
	def __init__(self, gpio):
		self.gpioPin = gpio
		self.servo = PWM.Servo()
		self.angle = 0
		self.pulseWidth = 0

	def setAngle(self, degrees):
		#http://www.raspberrypi.org/forums/viewtopic.php?f=44&t=36572
		pulse = 1520 + (degrees * 400) / 45
		
		if degrees > 90:
			degrees = 90
		elif degrees < -90:
			degrees = -90
		pulse = int(math.ceil(pulse / 10.0)) * 10	#round to nearest 10

		self.servo.set_servo(self.gpioPin, pulse)
		time.sleep(0.1)
		self.angle = degrees
		self.pulseWidth = pulse
		
	def incAngle(self, increment):
		self.setAngle(self.angle + increment)
	
	def cleanup(self):
		self.servo.stop_servo(self.gpioPin)

