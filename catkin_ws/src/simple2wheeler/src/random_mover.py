#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tämä laittaa robon liikkumaan satunnaisesti.
Julkaisee /random_mover/cmd_vel
tämä mapataan launch tiedostossa oikeaan paikkaan.
"""

import time
import random
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistWithCovarianceStamped

def MoveRandomAndPublish():
    """
    rotate z: -1 ... +1
    move   x: -1 ... +1
    """    
    TwistViestiUlos = Twist()
    
    TwistViestiUlos.angular.z = random.randint(-(abs(2)),abs(2))
    TwistViestiUlos.linear.x  = random.randint(-2,2)
    TwistViestiUlos.linear.y = 0.0
    TwistViestiUlos.linear.z = 0.0
    TwistViestiUlos.angular.x = 0.0
    TwistViestiUlos.angular.y = 0.0
    pub_twist.publish(TwistViestiUlos)

if __name__ == '__main__':
    rospy.init_node('random_mover', anonymous=False)

    pub_twist = rospy.Publisher("/random_mover/cmd_vel", Twist, queue_size=1)
    #pub_twist = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    
    print("random_mover loop")
    while not rospy.is_shutdown():
        #Power Nap
        time.sleep(0.05)
        MoveRandomAndPublish()
    print("loop exited, rospy shutdown")
