#!/usr/bin/env python
from flask import Flask, render_template, Response
import servo
import motor
import time

# emulated camera
#from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)

pan =servo.ServoController(25)
pan.setAngle(0)

tilt =servo.ServoController(24)
tilt.setAngle(0)

motorA = motor.MotorController(8,7)
motorB = motor.MotorController(10,9)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
					
@app.route("/<direction>")
def move(direction):
	# Choose the direction of the request
	if direction == 'panleft':
		pan.incAngle(10)
        
	elif direction == 'panright':
		pan.incAngle(-10)

	elif direction == 'tiltup':
		tilt.incAngle(-10)

	elif direction == 'tiltdown':
		tilt.incAngle(10)

	elif direction =='forward':
		motorA.start('F',100)
		motorB.start('F',100)
		time.sleep(0.5)
		motorA.stop()
		motorB.stop()
		
	elif direction =='reverse':
		motorA.start('B',100)
		motorB.start('B',100)
		time.sleep(0.5)
		motorA.stop()
		motorB.stop()

	elif direction =='right':
		motorA.start('F',100)
		motorB.start('B',100)
		time.sleep(0.5)
		motorA.stop()
		motorB.stop()

	elif direction =='left':
		motorA.start('B',100)
		motorB.start('F',100)
		time.sleep(0.5)
		motorA.stop()
		motorB.stop()

		
	return direction
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True)