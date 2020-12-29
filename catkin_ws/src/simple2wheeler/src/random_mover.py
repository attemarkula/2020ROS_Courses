#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Tämä laittaa robon liikkumaan satunnaisesti.
Julkaisee /random_mover/cmd_vel
tämä mapataan launch tiedostossa oikeaan paikkaan.
"""

import rospy

if __name__ == '__main__':
    rospy.init_node('random_mover', anonymous=False)

    pass

    
    
    
    
    
    
    print("random_mover spinning")
    while not rospy.is_shutdown():
       rospy.spin()
