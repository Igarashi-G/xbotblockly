#!/usr/bin/env python

import sys
import rospy
import subprocess
import rosnode
import numpy as np
import cv2
import time
import os
import rospkg	
from sensor_msgs.msg import Image

print("take a depth picture")

def take_depth_picture():
  command = "rostopic list"
  process = subprocess.Popen(command,shell = True, stdout = subprocess.PIPE)
  topic = process.communicate(input = None)
  if "/camera/depth/image_raw" in topic[0]:
    time_format = "%Y-%m-%d_%X.jpeg"
    timestr = time.strftime(time_format,time.localtime())
    
    msg_image = rospy.wait_for_message("camera/depth/image_raw", Image, timeout = 7)
    
    np_arr = np.fromstring(msg_image.data, np.uint8)
 #   print(np_arr,"type: ",type(np_arr))
 #   image_np = cv2.imdecode(np_arr, 1) 

    nrows, ncols = msg_image.height,msg_image.width

    print("encoding:",msg_image.encoding,"is_bigendian:",msg_image.is_bigendian,
"step:",msg_image.step)
    print("row:",ncols,"col:",nrows,"r*c:",ncols*nrows,"len:",len(msg_image.data))

    nparr = np.fromstring(np_arr, dtype=np.uint8).reshape(nrows, ncols, 4)
    image_np = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)#1
    
    #find path
    rospack = rospkg.RosPack()
    images_path = rospack.get_path('robot_blockly') + '/frontend/pages/depth_images/'
    
    #write picture to path
    cv2.imwrite(images_path+ 'depthimage_' + timestr, image_np, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    
    #amount of files in /frontend/images/ folder
    files = len(os.listdir(images_path))   
    if files > 7 : #allow 5 images max  
        os.system("find "+images_path+" -name '*.png' | xargs ls -t | tail -n 1 | xargs rm")#remove oldest image
  else:
    print("topic:\"/camera/depth/image_raw\" is not found!")  

take_depth_picture()
