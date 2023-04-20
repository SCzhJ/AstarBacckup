#! /usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
import math

x_ratio = 2.85/2.94
y_ratio = 1.0/1.0

init_val = -1000.00
zero_x = init_val
zero_y = init_val
zero_theta = init_val

pos_x = init_val
pos_y = init_val
ori_z = init_val
ori_theta = init_val

x, y, theta = 0.0, 0.0, 0.0

def changeOdometry(msg):
    global pos_x
    global pos_y
    global ori_z
    global ori_theta
    pos_x = msg.pose.pose.position.x
    pos_y = msg.pose.pose.position.y
    ori_z = msg.pose.pose.orientation.z
    if ori_z < 0:
        ori_z = 2.0 + ori_z
    ori_theta = ori_z * math.pi


if __name__ == "__main__":
    rospy.init_node("path_control_2")
    sub = rospy.Subscriber("odom", Odometry, changeOdometry, queue_size=100)
    rate = rospy.Rate(10)
    rate.sleep()
    while zero_x == init_val or zero_y == init_val or zero_theta == init_val:
        zero_x = pos_x
        zero_y = pos_y
        zero_theta = ori_theta

    rospy.loginfo("zero_x:%.2f, zero_y:%.2f, zero_theta:%.2f", zero_x, zero_y, zero_theta)

    cos_theta = math.cos(zero_theta)
    sin_theta = math.sin(zero_theta)

    while not rospy.is_shutdown():
        x = cos_theta * (pos_x - zero_x) + sin_theta * (pos_y - zero_y)
        y = -sin_theta * (pos_x - zero_x) + cos_theta * (pos_y - zero_y)
        x = x * x_ratio
        y = y * y_ratio
        theta = ori_theta - zero_theta
        rospy.loginfo("x:%.4f, y:%.4f, theta:%.4f, px: %.2f, py: %.2f, ori_z: %.2f, ori_theta: %.4f", x, y, theta, pos_x, pos_y, ori_z, ori_theta)

        rate.sleep()
