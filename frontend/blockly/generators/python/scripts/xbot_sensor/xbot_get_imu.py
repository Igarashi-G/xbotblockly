#!/usr/bin/env python

import rospy 
import subprocess
from sensor_msgs.msg import Imu

def get_Imu():
  command = "rostopic list"
  process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
  topic = process.communicate(input = None)

  if "/imu" in topic[0]:
    print("start get /imu data")
    msg_imu = rospy.wait_for_message("/imu", Imu, timeout = 1)
    print("orientation:",msg_imu.orientation)
    print("angular_velocity:",msg_imu.angular_velocity)
    print("linear_acceleration_covariance",msg_imu.linear_acceleration_covariance)
    print("linear_acceleration",msg_imu.linear_acceleration)

    return msg_imu.orientation
  else:
    print("topic:\"/imu\" is not found!")

msg_imu = get_Imu()
