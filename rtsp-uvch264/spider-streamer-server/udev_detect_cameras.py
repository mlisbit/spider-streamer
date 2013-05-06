#!/usr/bin/python
#the udev deamon that checks for all newly plugged/unplugged cameras

import glib
import gudev
import pynotify
import sys
import os
import start_streaming


#because there is no variable to display the node path from udev!
def get_node(devpath):
	nodepath = devpath[-6:]
	return str(nodepath)

def callback(client, action, device, user_data):

	if action == "add":
		 print "ADDED:" + get_node(device.get_property("DEVPATH"))
		 print "starting stream for device..."
		 #check to see if the camera matches "camera_make" is ssconfig 
		 if start_streaming.check_compatibility(get_node(device.get_property("DEVPATH"))):
		 	#starts the stream
		 	start_streaming.add_stream(get_node(device.get_property("DEVPATH")))
	#notifying you that the camera was unplugged 
	elif action == "remove":
		print "REMOVED:" + get_node(device.get_property("DEVPATH"))
		#when a stream ends, the port is still left open, so this will close it. 
		start_streaming.close_port(get_node(device.get_property("DEVPATH")))

client = gudev.Client(["video4linux"])
client.connect("uevent", callback, None)

loop = glib.MainLoop()
loop.run()

