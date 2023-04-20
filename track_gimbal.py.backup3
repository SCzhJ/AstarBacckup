#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from tf2_msgs.msg import TFMessage
from std_msgs.msg import Bool
import math

gimb_z = 0.0
direction = 0.0
sight = False

Interval = 5
Detection = [True] * Interval
detect_i = 0
track_on = False

def record_sight(msg):
    global sight
    sight = msg.data


def recordTF(msg):
    global gimb_z
    global direction
    if msg.transforms[0].child_frame_id == "gimbal":
        gimb_z = msg.transforms[0].transform.rotation.z
    if gimb_z > 0.0:
        direction = 1.0
    else:
        direction = -1.0


if __name__ == "__main__":
    rospy.init_node("track_gimbal")
    pub_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=100)
    pub_track = rospy.Publisher("/track_on", Bool, queue_size=100)
    sub_sight = rospy.Subscriber("/armor_in_sight", Bool, record_sight, queue_size=100)
    sub_tf = rospy.Subscriber("/tf", TFMessage, recordTF, queue_size=100)

    deltaTime = 0.1
    msg = Twist()
    msg.linear.x = 0.0
    msg.linear.y = 0.0
    msg.angular.z = 0.0

    rate = rospy.Rate(1/deltaTime)

    while not rospy.is_shutdown():
        if sight is True:
            track_on = True
            pub_track.publish(track_on)
            rate.sleep()
            msg.angular.z = direction * math.sqrt(direction * gimb_z) * 3
            pub_vel.publish(msg)
            Detection = [True] * Interval
            detect_i = 0
        else:
            Detection[detect_i] = False
            detect_i += 1
            if detect_i >= Interval:
                detect_i = 0
            rate.sleep()
        if set(Detection) == [False]:
            track_on = False
        pub_track.publish(track_on)

