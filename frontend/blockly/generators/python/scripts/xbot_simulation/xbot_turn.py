#!/usr/bin/env python

import rospy
import std_msgs.msg
from geometry_msgs.msg import Twist

def turn():
    
    turn_pub = rospy.Publisher("/cmd_vel_mux/input/navi",Twist,queue_size = 100)
    rate = rospy.Rate(20)
    msg = Twist()

    turn_vel = float(turn_speed)*3.1416/180
    if "left" is dropdown_direction:
        msg.angular.z = turn_vel
    else:
        msg.angular.z = -turn_vel

    turn_pub.publish(msg)

    print(msg)
    rate.sleep()

turn()
