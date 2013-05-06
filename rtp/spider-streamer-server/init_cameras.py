#!/usr/bin/python
#initial scan of the /dev/ directory to search for cameras already plugged in 
#author: Maciej Lis


import os
import start_streaming
from ssconfig import *

#array to hold all video nodes currently plugged in. 
currently_plugged_in = []

#scans /dev/ for all video# nodes plugged in 
for filename in os.listdir("/dev/"):
	if filename[0:5] == "video":
		currently_plugged_in.append(filename)

print currently_plugged_in

#this is a constand found in ssconfig
if webcam_present == True:
	currently_plugged_in.remove('video0')

print currently_plugged_in

#this will check to see if the camera matches the camera_make specified in ssconfig and makes a new list of compatible cameras
somelist = [camera_detected for camera_detected in currently_plugged_in if start_streaming.check_compatibility(camera_detected)]

#replaces the current list
currently_plugged_in = somelist

print currently_plugged_in

#start the stream for all cameras currently plugged in
for camera_detected in currently_plugged_in:
	start_streaming.add_stream(camera_detected)

#this will start the udev deamon to check for newly plugged/unplugged cameras
os.system("./udev_detect_cameras.py")
