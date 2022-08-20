#!/usr/bin/env python3

import rospy
import actionlib

from mars_rover.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult, Navigate2DGoal
from geometry_msgs.msg import Point


def feedback_callback(feedback):
    # How we handle the feedback from server, calling the name of the feedback specified in the action file
    print("Distance to goal: " + str(feedback.distance_to_point))



def nav_client(coordinates):
    # The name should be the same specified in the server
    client = actionlib.SimpleActionClient("navigate_2D_action", Navigate2DAction)
    client.wait_for_server()
    point_msg = Point(x = user_coordinates[0], y = user_coordinates[1], z = user_coordinates[2])
    # Navigation2DGoal takes as input a Point object
    goal = Navigate2DGoal(point_msg)
    client.send_goal(goal, feedback_cb = feedback_callback)
    client.wait_for_result()
    return client.get_result


if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try :
        rospy.init_node("navigate_2D_action_client_node")

        user_x = input("What is your desired x-coordinates? ")
        user_y = input("What is your desired y-coordinates? ")
        user_z = input("What is your desired z-coordinates? ")

        user_coordinates = [float(user_x), float(user_y), float(user_z)]

        result = nav_client(user_coordinates)
        print(result)

        rospy.spin()

    except rospy.ROSInterruptException:
    	print("Program interrupted.. :(")
