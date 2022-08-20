#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def rpm_sensor_pub():
   # This function takes a parameter that is the name of the node
   rospy.init_node("rpm_sensor_pub_node")
   # We publish (with a topic name) a message of type String, the queue_size are the number of messages that we can store (if exceeded, we drop the messages)
   pub = rospy.Publisher("/rpm", Float32 , queue_size = 10)
   
   rpm_sensor = 95.2
   rate = rospy.Rate(5)
   while not rospy.is_shutdown():
     pub.publish(rpm_sensor)
     # To control the rate at which we publish, we can use the rate
     rate.sleep()

if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try : 
    	rpm_sensor_pub()
    except rospy.ROSInterruptException:
    	pass
