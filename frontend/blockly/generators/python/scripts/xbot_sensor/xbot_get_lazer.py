#!/usr/bin/env python

import rospy
import subprocess
import rosnode
import rospkg
from sensor_msgs.msg import LaserScan

print("get_lazer")

def get_lazer():
  cmd = "rostopic list"
  process = subprocess.Popen(cmd,shell = True, stdout = subprocess.PIPE)
  topic = process.communicate(input = None)
  
  if "/scan" in topic[0]:
    print("start get /scan data ")
    msg_laser = rospy.wait_for_message("/scan",LaserScan,timeout = 1)
    ranges = msg_laser.ranges
    
    return ranges
    
  else:
    print("topic:\"/scan\" is not found!")

msg_laser = get_lazer()

