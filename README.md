spider-streamer
===============
Python & C

Decription
===============
Plug and play video steamer intended for use on a robots On Board Computer. 

The initial part of the program detects all currently plugged in cameras, and checks if theyre compatible, by their model number. If the camera is deemed compatible, an H.264 encoded stream in set up. 

Once all initially plugged in cameras are loaded, the program moves onto the "scanning mode", utilizing the udev deamon, and checks the events to see if any new cameras are plugged/unplugged. If a new compatible camera is detected a stream is set up on a new port. 

- port 4000 for camera plugged into /dev/video0 *(if it matches the specified make)*
- port 4001 for camera plugged into /dev/video1
- port 4002 for camera plugged into /dev/video2
- etc etc.. 

if the camera is not compatible, it is ignored. 

When a camera is unplugged or goes out of range, the clients video stream will freeze, and when reconnected, the stream will reinitialize. 

Requirements and Installation
---------------
Currently only used in Linux.
Will only work with cameras that have an embedded h.264 encoder, in the current state, but may be modified by changing the gstreamer command in start_streaming.py 

**v4l drivers** <br>

    $ sudo apt-get install v4l-utils 
    $ sudo apt-get install libv4l-dev
    $ sudo apt-get install qv4l2
    $ sudo apt-get install v4l2ucp

**gst streamer** <br>

    $ sudo apt-get install gstreamer-tools
    
**On the server side execute the init_cameras.py**

launch this command to pick up the stream, replace {port} with port


    gst-launch -v udpsrc port={port} caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' ! \ rtph264depay ! ffdec_h264 ! xvimagesink sync=false

Future Updates
---------------
- client side control
- camera/robot server will create its own webpage to host logs and controls
- get PyGST working 

Components 
---------------

**ssconfig.py** stores all the constants <br>
**udev_detect_cameras.py** the deamon that checks for newly plugged in/out cameras <br>
**start_streaming.py** determines how to set up the stream, and checks if the camera is compatible <br>
**init_cameras.py** te inital program you'd want to run, checks for all currently plugged in cameras <br>
**capture.c** is the source code to capture1, capture2, capture3 ... the only difference being is that the targeted video# node is different between each compiled version.
capture.c was not done by me, and I found the code here https://github.com/csete/bonecam/tree/master/capture 
<br>




