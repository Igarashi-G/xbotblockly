#!/usr/bin/env python

import time
import rospy
import std_msgs.msg
from geometry_msgs.msg import Twist

def move_time():
    
    move_time_pub = rospy.Publisher("/cmd_vel_mux/input/navi",Twist,queue_size = 100)
    msg = Twist()

    if "forward" is dropdown_direction:
    	msg.linear.x = float(move_speed)/100
    else:
    	msg.linear.x = -float(move_speed)/100
    
    rate = rospy.Rate(20)
    
    start_time = time.time()
    end_time = start_time + float(set_time)

    while not rospy.is_shutdown():
        #Exact to the second
        if round(time.time(),1) == round(end_time,1):
            break
        
        print(msg)
        move_time_pub.publish(msg)
        rate.sleep()

move_time()
