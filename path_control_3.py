#! /usr/bin/env python3

import rospy
from tf2_msgs.msg import TFMessage


trs_x = 0.0
trs_y = 0.0
trs_z = 0.0
rot_x = 0.0
rot_y = 0.0
rot_z = 0.0
rot_w = 0.0

def changeTF(msg):
    global trs_x
    global trs_y
    global trs_z
    global rot_x
    global rot_y
    global rot_z
    global rot_w
    if msg.transforms[0].child_frame_id == "base_link":
        trs_x = msg.transforms[0].transform.translation.x
        trs_y = msg.transforms[0].transform.translation.y
        trs_z = msg.transforms[0].transform.translation.z
        rot_x = msg.transforms[0].transform.rotation.x
        rot_y = msg.transforms[0].transform.rotation.y
        rot_z = msg.transforms[0].transform.rotation.z
        rot_w = msg.transforms[0].transform.rotation.w


if __name__ == "__main__":
    rospy.init_node("path_control_2")
    sub = rospy.Subscriber("tf", TFMessage, changeTF, queue_size=100)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("tx:%.4f,  ty:%.4f,  rz:%.6f", trs_x, trs_y, rot_z)
        rate.sleep()
