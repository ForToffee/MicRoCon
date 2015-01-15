import servo

pan =servo.ServoController(25)
tilt =servo.ServoController(24)

for deg in range(-90, 91,5):
	pan.setAngle(deg)
	tilt.setAngle(deg)
	