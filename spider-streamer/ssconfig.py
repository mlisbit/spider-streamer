#!/usr/bin/python
#page for storing all the constants, and configuration settings


#if you are testing this program on a laptop with a webcam present 
#the value should be true, to prevent streaming from it. 
#this assumes the webcam is module 'video0'
webcam_present = True

#extra cameras that may be plugged in that you do not wish to 
#execute this program on
webcam_exclude = []

#make of the camera you wish to stream from 
#you may get this by searching your lsusb, and looking for the name
camera_make = "C920"

#the IP of the machine you wish to SEND the stream to
client_machine_IP = "192.168.1.12" 

