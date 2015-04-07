#!/usr/bin/python
#Mike McCabe

import time
import picamera

cam = picamera.PiCamera()
cam.preview_fullscreen=False
cam.preview_window=(620, 320, 640, 480)
cam.start_preview()
while True:
	x = raw_input("Please enter a direction (f, r, l, b): ")
	if x == 'f':
		cam.capture('/home/pi/Tests/PiCam/front.jpg')
	elif x == 'r':
		cam.capture('/home/pi/Tests/PiCam/right.jpg')
	elif x == 'l':
		cam.capture('/home/pi/Tests/PiCam/left.jpg')
	elif x == 'b':
		cam.capture('/home/pi/Tests/PiCam/behind.jpg')
	else:
		break