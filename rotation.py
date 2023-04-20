#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from roborts_msgs.msg import GimbalAngle

if __name__ == "__main__":
    rospy.init_node("constant_move_p")
    pub_ch = rospy.Publisher("/cmd_vel", Twist, queue_size=100)
    pub_gi = rospy.Publisher("/cmd_gimbal_angle", GimbalAngle, queue_size=100)
    Period = 0.05 
    rate = rospy.Rate(1/Period)
    Speed = 0.4
    msg = Twist()
    msg.linear.x = 0.0
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = Speed
    msg_gimbal = GimbalAngle()
    msg_gimbal.yaw_angle = 3.0
    while not rospy.is_shutdown():
        #pub_ch.publish(msg)
        pub_gi.publish(msg_gimbal)
        #msg_gimbal.yaw_angle += -Period * Speed
        rate.sleep()
