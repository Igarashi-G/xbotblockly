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
# Ros Messages	 
from sensor_msgs.msg import CompressedImage

print("take a picture!")
'''
话题：/camera/rgb/image_raw/compressed
结构体:
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string format
uint8[] data

'''

time_format = "%Y-%m-%d_%X.png"
timestr = time.strftime(time_format,time.localtime())#设置时间



ros_nodes = rosnode.get_node_names()#获取节点名称
if '/raspicam_node' in ros_nodes:#判断是否存在
    command='rosservice call /camera/start_capture'#要执行的命令
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)#开启子线程
else:
    command='/home/erle/ros_catkin_ws/install_isolated/camera.sh'#不存在调用.sh文件
    command+=';rosservice call /camera/start_capture'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)#无论如何都要执行这条命令

msg_image = rospy.wait_for_message('/camera/image/compressed', CompressedImage, timeout=7)#等待话题的响应，超时7s
np_arr = np.fromstring(msg_image.data, np.uint8)#获取图像数据并转换为一个无符整型的矩阵
image_np = cv2.imdecode(np_arr, 1) #cv2.CV_LOAD_IMAGE_COLOR 将矩阵解码即为对应的图片数据


rospack = rospkg.RosPack()#使用默认搜索路径获取一个RosPack实例
images_path = rospack.get_path('robot_blockly') + '/frontend/pages/images/'#获取robot_blockly/frontend/pages/images/路径
cv2.imwrite(images_path+ 'image_' + timestr, image_np)#写入了图片数据到指定路径下

#cv2.imwrite('/home/erle/spider_ws/install_isolated/share/robot_blockly/frontend/pages/images/image_' + timestr, image_np)
#images_path = "/home/erle/spider_ws/install_isolated/share/robot_blockly/frontend/pages/images/"

files = len(os.listdir(images_path)) #amount of files in /frontend/images/ folder  这里是记什么数的

if files > 7 : #allow 5 images max  若上面计数超过7
    os.system("find "+images_path+" -name '*.png' | xargs ls -t | tail -n 1 | xargs rm")#remove oldest image
#则用指令删除图片
command="rosservice call /camera/stop_capture" #要执行的命令2
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
