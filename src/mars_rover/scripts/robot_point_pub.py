#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point

if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try :
        # This function takes a parameter that is the name of the node
        rospy.init_node("robot_point_pub_node")
        # We publish (with a topic name) a message
        pub = rospy.Publisher("robot_point", Point , queue_size = 10)

        user_x = input("What is your desired x-coordinates? ")
        user_y = input("What is your desired y-coordinates? ")
        user_z = input("What is your desired z-coordinates? ")

        point = Point(x = float(user_x), y = float(user_y), z = float(user_z))

        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
          pub.publish(point)
          # print(point)
          # To control the rate at which we publish, we can use the rate
          rate.sleep()


    except rospy.ROSInterruptException:
    	pass
