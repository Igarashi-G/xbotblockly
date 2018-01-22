#!/usr/bin/env python

print('xbot begin to move')

import time
import rospy
import std_msgs.msg
from geometry_msgs.msg import Twist
   

################
## INITIALIZE ##
################ 
pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=100)

msg = Twist()
turn_vel = float(turn_speed)*3.1416/180
if "left" is dropdown_direction:
 msg.angular.z = turn_vel
else:
 msg.angular.z = -turn_vel

rate = rospy.Rate(20)

################
##    MOVE    ##
################ 
start_time = time.time()
end_time = start_time + float(turn_time)
	
while not rospy.is_shutdown():
 if round(time.time(),1) == round(end_time,1):
  break

 pub.publish(msg)
 rate.sleep() 

