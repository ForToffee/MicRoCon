# MicRoCon

Tinkering with a MicRoCon v1.1 from 4Tronix and a Pan & Tilt from AdaFruit.  For the most part I've consumed work by others to create the system I envisioned.  Sources cited below

app.py
------
Main Flask application/server [2] & [3]
- creates and monitors camera object
- manages commands to move camera or motors
- runs threaded so both camera and http requests from buttons can be actioned [4]

camera_pi.py
------------
Raspberry Pi camera module interface [2]

motor.py
--------
Motor controller class - bit basic at the moment, would like to add PWM

servo.py
--------
Servo controller class 

#Requirements
Flask - sudo pip install flask
RPIO - sudo pip install rpio 

#Sources
[1] http://blog.miguelgrinberg.com/post/video-streaming-with-flask
[2] https://github.com/miguelgrinberg/flask-video-streaming
[3] http://arusahni.net/blog/2013/10/flask-multithreading.html
[4] http://makezine.com/projects/raspberry-eye-remote-servo-cam/
