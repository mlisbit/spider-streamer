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
	os.system("v4l2-ctl -d /dev/video"+node_number+" --set-parm=30")
	#starts the stream, and records output to a log.txt file
	os.system("./rtsp "+dev_path+" &")

def close_port(dev_path):
	#when a stream ends, the port is still left open, so this will close it. 
	print "Closing port for: " + dev_path
	node_number = dev_path[-1]
	node_number = int(node_number)
	node_number += 8550
	
	start_capture = os.popen("netstat -lpn | grep " + str(node_number)) 			#terminal command executed 
	s = start_capture.readlines()								#gets the output
	start_capture.close()									#stops capturing the input
	process_string = ''.join(s);									
	
	if (process_string.find("LISTEN") != -1):						#checks if this string is found
		start = int(process_string.index("LISTEN")+6)
		process_ID = ""
		while (process_string[start] != '/'):
			process_ID += str(process_string[start])
			start=start+1
		process_ID = "".join(process_ID.split())
		print "killing process ID: " +process_ID
		os.system("kill " + process_ID)
	
	
	
	
	
	

	
