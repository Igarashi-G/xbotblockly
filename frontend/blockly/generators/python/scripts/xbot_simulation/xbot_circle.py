#!/usr/bin/env python

import time
import rospy
import std_msgs.msg
from geometry_msgs.msg import Twist

def move_circle():
    print("circle!")
    move_time_pub = rospy.Publisher("/cmd_vel_mux/input/navi",Twist,queue_size = 100)
    msg = Twist()
    
    if "clockwise" is clock_direction:
    	msg.linear.x = float(move_speed)/100
    else:
    	msg.linear.x = float(move_speed)/100
    
    if "left" is direction:
        msg.angular.z = float(turn_speed) * 3.1416 / 180
    else:
        msg.angular.z = -float(turn_speed)* 3.1416 / 180

    rate = rospy.Rate(20)
	
    while not rospy.is_shutdown():
       
        move_time_pub.publish(msg)
        rate.sleep()

move_circle()
    
