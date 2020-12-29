#!/usr/bin/python3
import rospy
from geometry_msgs.msg import TwistWithCovarianceStamped
from turtlesim.msg import Pose
import tf2_ros
import turtlesim
import random


random_noise_linear = 0.02
systemic_noise_linear = 0.2
random_noise_angular = 0.02
systemic_noise_angular = 0.2

#1/10 default, jotta pysyy joukko kasassa.
#random_noise_linear = 0.001
#systemic_noise_linear = 0.01
#random_noise_angular = 0.001
#systemic_noise_angular = 0.01


def pose_call_back(msg):
    twist_to_send = TwistWithCovarianceStamped()
    twist_to_send.header.seq = twist_to_send.header.seq +1
    twist_to_send.header.stamp = rospy.Time.now()
    twist_to_send.header.frame_id = "base_link"
    
    twist_to_send.twist.twist.linear.x = msg.linear_velocity*(1+systemic_noise_linear+random.uniform(0, random_noise_linear))
    twist_to_send.twist.twist.linear.y = 0.0
    twist_to_send.twist.twist.linear.z = 0.0
    twist_to_send.twist.twist.angular.x = 0.0
    twist_to_send.twist.twist.angular.y = 0.0
    twist_to_send.twist.twist.angular.z = 0.0
    twist_to_send.twist.twist.angular.z = msg.angular_velocity*(1+systemic_noise_angular+random.uniform(0, random_noise_angular))
    twist_to_send.twist.covariance = systemic_noise_linear, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,systemic_noise_angular
    pub_twist.publish(twist_to_send)

if __name__ == '__main__':
    print("Running now.")
    rospy.init_node("turtle_odometry")
    pub_twist = rospy.Publisher('turtle1/sensor/twist', TwistWithCovarianceStamped, queue_size=1)
    rospy.Subscriber("turtle1/pose", Pose, pose_call_back)
    rospy.spin()
