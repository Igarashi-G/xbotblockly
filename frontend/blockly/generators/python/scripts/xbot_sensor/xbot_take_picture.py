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
from sensor_msgs.msg import CompressedImage

print("take a picture!")

def take_picture():
  cmd = "rostopic list"
  process = subprocess.Popen(cmd,shell = True, stdout = subprocess.PIPE)
  topic = process.communicate(input = None)

  if "/camera/rgb/image_raw/compressed" in topic[0]:
    
    time_format = "%Y-%m-%d_%X.png"
    timestr = time.strftime(time_format,time.localtime())
  
    msg_image = rospy.wait_for_message("/camera/rgb/image_raw/compressed", CompressedImage, timeout=7)
  
    #get CompressedImage data
    np_arr = np.fromstring(msg_image.data, np.uint8)
    image_np = cv2.imdecode(np_arr, 1) 
    
    #find path
    rospack = rospkg.RosPack()
    images_path = rospack.get_path('robot_blockly') + '/frontend/pages/images/'
    
    #write picture to path
    cv2.imwrite(images_path+ 'image_' + timestr, image_np)
    
    #amount of files in /frontend/images/ folder
    files = len(os.listdir(images_path))   
    if files > 7 : #allow 5 images max  
        os.system("find "+images_path+" -name '*.png' | xargs ls -t | tail -n 1 | xargs rm")#remove oldest image
  else:
    print("topic:\"/camera/rgb/image_raw/compressed\" is not found!")
  
take_picture()




