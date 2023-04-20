#! /usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry


#pos_x = 0.0
#pos_y = 0.0
#pos_z = 0.0
#ori_x = 0.0
#ori_y = 0.0
ori_z = 0.0
ori_w = 0.0
old_z = 0.0
d_z = 0.0
old_w = 0.0
d_w = 0.0
old_ratio = 0.0
ratio = 0.0
d_ratio = 0.0

def changeOdometry(msg):
    #global pos_x
    #global pos_y
    #global pos_z
    #global ori_x
    #global ori_y
    global ori_z
    global ori_w
    #pos_x = msg.pose.pose.position.x
    #pos_y = msg.pose.pose.position.y
    #pos_z = msg.pose.pose.position.z
    #ori_x = msg.pose.pose.orientation.x
    #ori_y = msg.pose.pose.orientation.y
    ori_z = msg.pose.pose.orientation.z
    ori_w = msg.pose.pose.orientation.w


if __name__ == "__main__":
    rospy.init_node("path_control_4")
    sub = rospy.Subscriber("odom", Odometry, changeOdometry, queue_size=100)
    rate = rospy.Rate(10)
    #counter = 0
    while not rospy.is_shutdown():
        d_w = ori_w - old_w
        d_z = ori_z - old_z
        #if d_w != 0.0 or d_z != 0.0:
        #    ratio = d_z / d_w
        #    d_ratio = ratio - old_ratio
        #    rospy.loginfo("interval:%.d,ratio:%.6f,d_ratio:%.6f",counter,ratio,d_ratio)
        #    old_ratio = ratio
        #    counter = 0
        rospy.loginfo("oz:%.4f,ow:%.4f,d_z:%.6f,d_w:%.6f",ori_z,ori_w,d_z,d_w)
        old_z = ori_z
        old_w = ori_w
        #counter += 1
        rate.sleep()
