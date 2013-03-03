#!/usr/bin/python
#pick which stream you wish to view 
#this file is just a temporary "stream picker" - until I come up with a new one

import os

print "0 - start stream from video0"
print "1 - start stream from video1"
print "2 - start stream from video2"
print "3 - start stream from video3"
print "4 - start stream from video4"

user_input = int(raw_input("Enter Number: "))
user_input = str(user_input)

os.system("gst-launch -v udpsrc port=400"+user_input+" caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' ! \ rtph264depay ! ffdec_h264 ! xvimagesink sync=false > log.txt &")


