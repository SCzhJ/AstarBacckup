#!/usr/bin/env python3

import rospy
import math
import random
from geometry_msgs.msg import Twist
from roborts_msgs.msg import GimbalAngle

if __name__ == "__main__":

    rospy.init_node("constant_move_p")
    pub_ch = rospy.Publisher("/cmd_vel", Twist, queue_size=100)
    pub_gi = rospy.Publisher("/cmd_gimbal_angle", GimbalAngle, queue_size=100)

    Period = 0.05 
    rate = rospy.Rate(1/Period)
    Speeds = [0.0, 1.0, 2.0, 3.0, 3.5]
    Speed = Speeds[2]
    RotationPeriod = 1.0
    RotationCountdown = RotationPeriod
    Direction = 1.0

    msg = Twist()
    msg.angular.z = Speed * Direction
    msg_gimbal = GimbalAngle()
    msg_gimbal.yaw_angle = 0.0

    while not rospy.is_shutdown():
        if RotationCountdown <= 0.0:
            if random.random() < 0.9:
                if (Speed == Speeds[0] or Speed == Speeds[1]) and random.random() < 0.5:
                    Direction = -Direction
                Speed = random.choice(Speeds, weights=(0.2, 0.1, 0.15, 0.25, 0.3), k=5)
                msg.angular.z = Speed * Direction
            RotationCountdown = RotationPeriod + random.random() * Speed
        RotationCountdown -= Period
        pub_ch.publish(msg)
        rate.sleep()
