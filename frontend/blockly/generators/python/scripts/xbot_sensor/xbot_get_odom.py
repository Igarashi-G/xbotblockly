#!/usr/bin/env python
import rospy,subprocess
from nav_msgs.msg import Odometry

def get_Odometry():
  command = "rostopic list"
  process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
  topic = process.communicate(input = None)
  if "/odom" in topic[0]:
    print("start get /odom data")
    msg_odom = rospy.wait_for_message("/odom",Odometry,timeout = 1)
    print(msg_odom.twist.twist.linear)
    print(msg_odom.twist.twist.angular)
    print(msg_odom.pose.pose.position)
    return msg_odom.pose.pose.position
  else:
    print("topic :\"/odom\" is not found!")

msg_odom = get_Odometry()
