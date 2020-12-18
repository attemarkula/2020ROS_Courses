#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Lisää / spawnaa alueen etäisyys turtle2, sama kuin mitä turtle2 on turtle1
1 --- 2 ---3 
ei kielletty, määrätään staattisesti etäisyydet. Näillä aamuilla liian vaikeaa selvittää nodeista.
Muutaa turtle2 viivan helpommin eroitettavaksi
Lukee turtle1/sensor/twist tiedot ja julkaisee ne turtle2/cmd_vel, tämä saa turtle2 liikkumaan.
"""
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import turtlesim
import turtlesim.srv

def twist_callback(msg):
    twist_to_turtle3 = Twist()
    twist_to_turtle3.linear.x = msg.twist.twist.linear.x
    twist_to_turtle3.angular.z = msg.twist.twist.angular.z
    pub_twist.publish(twist_to_turtle3)

if __name__ == '__main__':
    #odota että service käynnissä
    rospy.wait_for_service('spawn')
    #spawn uusi turtle
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    #määritä missä asennossa turtle on
    #spawner(5.544,5.544,0,'turtle3')
    spawner(3.544, 3.544, 0, 'turtle3')
    # jotta erottaa paremmin.
    pen_setter = rospy.ServiceProxy('/turtle3/set_pen', turtlesim.srv.SetPen)
    pen_setter(128,255,255,1,0)
    
    


    
    rospy.init_node("turtle3_twist_remapper_node")
    #tilaa mitä kuunnellaan ja liitä käsittelijä viesteille
    rospy.Subscriber("odometry/filtered_twist", Odometry, twist_callback)
    #lähetä omat jutut turtle3:lle 
    pub_twist = rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=1)

    #tämä pitää prosessin pyörimässä, eikä lopeta kertaan.
    rospy.spin()
