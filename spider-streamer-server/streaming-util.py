#!/usr/bin/python
# This program starts an ad-hoc connection
# Author: Maciej Lis

import os
essid = "webcamserver"
loginkey = "1234567890"
interface = "wlan0"
client_machine_IP = "192.168.1.7" 

def option_one():
	os.system("sudo service network-manager stop")
	os.system("sudo ip link set " + interface + " down")
	os.system("sudo iwconfig " + interface + " mode ad-hoc") 
	os.system("sudo iwconfig " + interface + " channel 4")
	os.system("sudo iwconfig " + interface + " essid '" + essid + "'")
	os.system("sudo iwconfig " + interface + " key " + loginkey)
	#ReEstablishing the card
	os.system("sudo ip link set " + interface + " up")
	os.system("sudo ip addr add 192.168.1.2/16 dev " + interface)
	
print "1 - start your adhoc connection (server)"
print "2 - stop your adhoc and re-enable network manager service"
print "3 - ping machine"
print "4 - start streaming"
print "5 - stop streaming"
print "6 - capture stream (client)"
print "10 - exit"
 
user_input = int(raw_input("Enter Number: "))

if user_input == 1:
	option_one()
if user_input == 2:
	os.system("service network-manager start")
if user_input == 3: #ping the client machine
	os.system("ping " + client_machine_IP)
if user_input == 4:
	os.system("./capture -c 10000 -o | gst-launch -v -e filesrc location=/dev/fd/0 ! h264parse ! rtph264pay ! udpsink  host=" + client_machine_IP + " port=4000")
if user_input == 5:
	pass
if user_input == 6:
	os.system("gst-launch -v udpsrc port=4000 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' ! \ rtph264depay ! ffdec_h264 ! xvimagesink sync=false")
if user_input == 10:
	print "goodbye"
	quit()





