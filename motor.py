import RPIO 
import time
import math

class MotorController:
	def __init__(self, gpio1, gpio2):
		self.gpioPinA = gpio1
		self.gpioPinB= gpio2
		RPIO.setup(gpio1, RPIO.OUT, initial=RPIO.LOW)
		RPIO.setup(gpio2, RPIO.OUT, initial=RPIO.LOW)

		#self.servo = PWM.Servo()
		#self.angle = 0
		#self.pulseWidth = 0

	def start(self, direction, speed, duration=0):
		#http://www.raspberrypi.org/forums/viewtopic.php?f=44&t=36572
		if direction == 'F':
			RPIO.output(self.gpioPinA, True)
			RPIO.output(self.gpioPinB, False)
		else:
			RPIO.output(self.gpioPinA, False)
			RPIO.output(self.gpioPinB, True)
		
		if duration > 0:
			time.sleep(duration)
			self.stop()
			
	def stop(self):
		RPIO.output(self.gpioPinA, False)
		RPIO.output(self.gpioPinB, False)
		
	

