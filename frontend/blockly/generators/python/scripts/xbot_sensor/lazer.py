#!/usr/bin/env python
#-*- coding:utf8-*--

import rospy
import subprocess
import rosnode
import rospkg
from sensor_msgs.msg import Range

print("get_lazer")
ros_nodes = rosnode.get_node_names()#get node
if not '/lrm30_node' in ros_nodes:
  rospack = rospkg.RosPack()#使用默认搜索路径获取RosPack的一个实例
  command = rospack.get_path('lrm30_ros').replace('share', 'lib') + '/lrm30'
  #用来获取路径，替换路径share为lib 后+lrm30 即/lib/lrm30_ros/lrm30
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)#创建一个新的进程
  #command 执行命令
  #shell = True 程序由shell来执行 
  #stdout 表示程序的标准输出 PIPE Permission denied权限被拒绝
msg_laser = rospy.wait_for_message('/lrm30_data', Range, timeout=1)#等待data range数据类型 超时1s

def callback(LaserScan):
  scan_data = LaserScan
  scan_ranges = scan_data.ranges
  print(scan_data)#是否可以开启子线程来一直调用这个callback

#rospy.Subscriber("/scan",LaserScan,callback)
