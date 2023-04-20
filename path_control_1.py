#! /usr/bin/env python3

import rospy
#from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


pos_x = 0.0
pos_y = 0.0
pos_z = 0.0
ori_x = 0.0
ori_y = 0.0
ori_z = 0.0

def changeOdometry(msg):
    global pos_x
    global pos_y
    global pos_z

    global ori_x
    global ori_y
    global ori_z
    
    pos_x = msg.pose.pose.position.x
    pos_y = msg.pose.pose.position.y
    pos_z = msg.pose.pose.position.z
    ori_x = msg.pose.pose.orientation.x
    ori_y = msg.pose.pose.orientation.y
    ori_z = msg.pose.pose.orientation.z

if __name__=="__main__":
    rospy.init_node("path_control_1")
    sub = rospy.Subscriber("odom",Odometry,changeOdometry,queue_size=100)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("px:%.2f, py:%.2f, pz:%.2f, ox:%.2f, oy:%.2f, oz:%.2f",pos_x,pos_y,pos_z,ori_x,ori_y,ori_z)
        rate.sleep()
    


