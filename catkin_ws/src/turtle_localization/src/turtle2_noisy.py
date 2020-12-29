#!/usr/bin/python3
"""
ohjaa turtlea
"""
import rospy
from geometry_msgs.msg import TwistWithCovarianceStamped
from geometry_msgs.msg import Twist
import turtlesim.srv
import turtlesim

def twist_call(msg):
    twist_to_turtle2 = Twist()
    twist_to_turtle2.linear.x = msg.twist.twist.linear.x
    twist_to_turtle2.angular.z = msg.twist.twist.angular.z

    pub_twist.publish(twist_to_turtle2)

    
    #ohjaa turtlea

if __name__ == "__main__":
    print("Running...")
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5.544,5.544,0,"turtle2")
    
    rospy.wait_for_service('/turtle2/set_pen')
    pen_setter = rospy.ServiceProxy('spawn',turtlesim.srv.Spawn)
    pen_setter = rospy.ServiceProxy('/turtle2/set_pen', turtlesim.srv.SetPen)
    pen_setter(0,0,0,5,0)
    

    rospy.init_node("turtle2_twist_remapper_node")
    rospy.Subscriber("turtle1/sensor/twist", TwistWithCovarianceStamped, twist_call)
    pub_twist = rospy.Publisher("turtle2/cmd_vel", Twist, queue_size=1)
    rospy.spin()

