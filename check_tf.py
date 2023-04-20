#!/usr/bin/env python

import rospy
import math
import random
from geometry_msgs.msg import Twist
from roborts_msgs.msg import GimbalAngle
from tf2_msgs.msg import TFMessage
from std_msgs.msg import Bool


gimb_z = 0.0

def record_tf(msg):
    global gimb_z
    if msg.transforms[0].child_frame_id == "gimbal":
        gimb_z = msg.transforms[0].transform.rotation.z


if __name__ == "__main__":

    rospy.init_node("check_tf")

    sub_tf = rospy.Subscriber("/tf", TFMessage, record_tf, queue_size=100)

    Period = 0.1 
    rate = rospy.Rate(1/Period)

    while not rospy.is_shutdown():
        rospy.loginfo(gimb_z)
        rate.sleep()
