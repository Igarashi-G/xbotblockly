#!/usr/bin/env python

import rospy,rospkg
import time
import subprocess
import numpy as np
import cv2
import sys
import os
from sensor_msgs.msg import PointCloud2

print("take a depth picture")

def take_depth_picture():
  command = "rostopic list"
  process = subprocess.Popen(command,shell = True, stdout = subprocess.PIPE)
  topic = process.communicate(input = None)
  if "/camera/depth/points" in topic[0]:
    time_format = "%Y-%m-%d_%X"
    timestr = time.strftime(time_format,time.localtime())
    
    print("take start")
    msg_image = rospy.wait_for_message("camera/depth/points", PointCloud2, timeout = 7)
    
    np_arr = np.fromstring(msg_image,np.uint8)
    image_np = cv2.imdecode(np_arr, 1)

    rospack = rospkg.RosPack()
    images_path = rospack.get_path("robot_blockly") + "/frontend/pages/depth_images"

    cv2.imwrite(images_path + "depthImage_" + timestr,image_np)

    files = len(os.listdir(images_path))

    if files > 7:
      os.system("find " +images_path + " -name '*.png' | xargs ls -t | tail -n 1 | xargs rm")
  else:
    print("topic:\"/camera/depth/points\" is not found!")  

take_depth_picture()
