#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3

if __name__ == "__main__":
    rospy.init_node("location_sender")
    pub = rospy.Publisher("/location", Vector3, queue_size=100)
    rate = rospy.Rate(1)
    msg = Vector3()
    msg.x = 0.0
    msg.y = 0.0
    msg.z = 0.0
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()
