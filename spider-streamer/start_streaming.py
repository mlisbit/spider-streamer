#!/usr/bin/python

import os
import sys
from ssconfig import *
def check_compatibility(dev_path):
	node_number = dev_path[-1]

	#scans the output from v4l2-ctl to see if the camera inputed matches the specified "camera_make in ssconfig
	get_output = os.popen("v4l2-ctl --device="+node_number+" -D")
	s = get_output.readlines()
	get_output.close()
	device_info = ''.join(s);

	if device_info.find(camera_make) > 0:
		return True
	return False

def add_stream(dev_path):
	print "The arguement provided is: " + dev_path
	node_number = dev_path[-1]
	os.system("v4l2-ctl -d /dev/video"+node_number+" --set-fmt-video=width=800,height=448,pixelformat=1")
	os.system("v4l2-ctl -d /dev/video"+node_number+" --set-parm=30")
	#starts the stream, and records output to a log.txt file
	os.system("./capture"+node_number+" -c 10000 -o | gst-launch -v -e filesrc location=/dev/fd/0 ! h264parse ! rtph264pay ! udpsink  host=" + client_machine_IP + " port=400"+node_number+" > log.txt &")

	
	
	
	
	
	

	
