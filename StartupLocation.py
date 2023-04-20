#!/usr/bin/env python

import rospy
import math
import random
from geometry_msgs.msg import Twist
#from roborts_msgs.msg import GimbalAngle
#from tf2_msgs.msg import TFMessage
from std_msgs.msg import Bool

if __name__ == "__main__":

    rospy.init_node("startup_location")
    pub_topos = rospy.Publisher("/to_position", Bool, queue_size=100)
    pub_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=100)


    deltaTime = 0.1
    rate = rospy.Rate(1/deltaTime)
    Time = 1.5
    msg = Twist()
    msg.linear.x = 0.0
    msg.linear.y = 0.0
    pub_topos.publish(False)

    while (not rospy.is_shutdown()) and (Time >= 0):
        pub_vel.publish(msg)
        Time -= deltaTime
        pub_topos.publish(False)
        rate.sleep()

    msg.linear.x = 0.0
    msg.linear.y = 0.0
    pub_topos.publish(True)
    pub_vel.publish(msg)
    rate.sleep()
    pub_topos.publish(True)
    pub_vel.publish(msg)
    rate.sleep()
    pub_topos.publish(True)
    pub_vel.publish(msg)
