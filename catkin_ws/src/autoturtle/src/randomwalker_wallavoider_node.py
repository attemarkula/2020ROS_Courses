#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist

#koska subsc paikkatietoon
from turtlesim.msg import Pose

import random

#callback funktio ajetaan, kun Pose lähettää arvon.

def callback(data):
    """
    datan saapuessa suoritettava funktio,
    koodi välttää seiniä, seuraamalla pose.x arvoa.
    """
    vel_msg = Twist()
    pose = data

    if pose.x > 10:
        vel_msg.angular.z = 0
        vel_msg.linear.x  = -2
    elif pose.x < 1:
        vel_msg.angular.z = 0
        vel_msg.linear.x  = +2
    elif pose.y > 10:
        vel_msg.angular.z = 0
        vel_msg.linear.x  = -2
    elif pose.y < 1:
        vel_msg.angular.z = 0
        vel_msg.linear.x  = +2
    else:
        vel_msg.angular.z = random.randint(-2,2)
        vel_msg.linear.x  = random.randint(0,2)

    velocity_publisher.publish(vel_msg)

rospy.init_node('turtlebot_auto', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)

while not rospy.is_shutdown():
    rospy.spin()


