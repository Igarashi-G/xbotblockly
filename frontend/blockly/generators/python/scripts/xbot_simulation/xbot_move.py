#!/usr/bin/env python

import rospy
import std_msgs.msg
from geometry_msgs.msg import Twist

def talker():
    #rospy.init_node("up_node")
    move_pub = rospy.Publisher("/cmd_vel_mux/input/navi",Twist,queue_size = 100)
    rate = rospy.Rate(20)
    
    msg = Twist() 
    if "forward" is dropdown_direction:
        msg.linear.x = float(move_speed)/100
    else:
        msg.linear.x = -float(move_speed)/100

#    while not rospy.is_shutdown():
#        rospy.info("Talker: move: x = %f"% msg.linear.x)
    for i in range(3):
        move_pub.publish(msg)

        print(msg)
        rate.sleep()

talker()

