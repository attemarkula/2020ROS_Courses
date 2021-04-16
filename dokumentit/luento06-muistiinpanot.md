# koordinaatiojärjestelmät, kuudes luento, 20201112


##TF2

node kuuntelee muutoksia
node julkaisee muutokset

yaw moves left right
pitch up or down
roll over

#gimpal lock
gimbal lock kun kaksi ovat yhdessä.



kvaternion kompleksilukujen laajennos neljänteen ulottuvuuteen

kompleksi lukujen esitys
1D = 2 yksi ylotteinen piste
2D 2+3i
3D ei olemassa, vaan nämä esitetään 4D kautta
4D 2+3i+2k+4j neljäs uloittuvuus




koordinaatti kvarternioniksi ja takaisin



Workshop

catkin_create_pkg tf2_harjoitus tf2_ros roscpp rosp turtlesim


## turtle_tf2_broadcaster.py

tehdään handleri
initialisoidaan node
tilataan pose
haetaan parametri


TransformStamped sisältää:
header joka sisältää
	frame_id -> vanhemman associaatio
	child_frame_id jos niitä on
	tranform:in jossa on 
		vektor3 (x,y,z) siirros
		Quaternion rotaatio (x,y,z,w)


t=geometry_msgs.msg.TransformStamped()
t.header.frame_id = "world"
t.child_frame_id = turtlename


Tämä ohjelma julkaisee /tf mnoden kautta  


## launch tiedosto

lisättiin parametri joka luettiin turtle_tf2_broadcaster.py:ssä

turtlename=rospy.get_param('~turtle')



### debuggausta

jos broadcaster rikki, niin 
rostopic echo /tf
sanoo ettei sitä ole julkaistu.


parametriserveri hanskaa pamatetrit
$ rosparam list
tämä näyttää listan kaikista parametreistä, esim.
turtle1_tf2_broadcaster/turtle

$ rosparam get /turtle1_tf2_broadcaster/turtle
tämä palauttaa tekstin:
turtle1

tämä tarkastaa että parametri serverillä on mennyt kaikki oikein.

rosparam pystyy myös vaihtamaan konsolilta suoraan asetuksia.


### rosservice
topic:in ja server client ero on että silloin menee yhdeltä yhdelle.
lähetys <-> vastaus


$ rosservice list

listaa kaikki servicet

$ rosservice info /spawn

kertoo tiedot spawnin tiedot.
(googlaa turtlesim/Spawn)
kertoo mitä input ja mitä output


$ rosservice call /spawn
ja paina tabulaattoria ja täytä tiedot.

Tämä teki uuden turtle2:n kentälle.


$ rosservice info /kill

$ rosservice call /kill "name: 'turtle2'"

tämä poisti turtle2:den kentältä


## turtle_tf2_listener.py

luotiin init_node 'tf2_turtle_listener'

rospy.wait_for_service('spawn')
tämä rivi odottaa että palvelu "spawn" on käytössä.

spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
turtle_name = rospy.get_param('turtle', 'turtle2')

spawner(x,y,theta,name) 
tämä luo uuden turtlen kentälle em. tiedoilla.


turtle_vel = rospy.Publisher('%s/cmd' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
rate=rospy.Rate(10.0)
tämä määrää 10 kertaa sekunnissa tiedon lähetettäväksi

ja sitten tehtiin try-catch jossa tfbufferista etsittiin transformista aika?
except lista virheistä, niin silloin rate.sleep() ja continue


jne jne... lopputulos on toinen turtle joka lukee edellisen turtlen paikan ja seuraa sitä perässä.

ja hyödyllistä on myös katsoa 

rosrun rqt_graph rqt_graph
näkee että yhteys on 
/teleop -> /sim
/sim -> t2_tf2_broadcaster -> /listener
/sim -> t1_tf2_broadcaster -> /listener
/listener -> /sim


