#!/usr/bin/env python3

import rospy
import actionlib
import math
from mars_rover.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point

class Navigate2DClass():
    def __init__(self):
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action", Navigate2DAction, self.navigate_cb)
        self.robot_point_sub = rospy.Subscriber("robot_point", Point, self.update_robot_position)
        self.robot_current_point = None
        self.robot_goal_point = None
        self.distance_treshold = 0.35
        self.feedback_rate = rospy.Rate(2)

    def update_robot_position(self, point):
        self.robot_current_point = [point.x, point.y, point.z]

    # Callback function to set the goal
    def navigate_cb(self, goal):
        navigate_start_time = rospy.get_time()
        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]

        # This loop avoid subscribing before a point have been published
        while self.robot_current_point == None:
            print("Robot point not detected!")
            rospy.sleep(5)
        print("Robot point detected!")
        distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)
        # We continue to publish a feedback to tell how fare we are (simulating the movement) and this is the feedback
        while distance_to_goal > self.distance_treshold:
            self.action_server.publish_feedback(Navigate2DFeedback(distance_to_point = distance_to_goal))
            # This to avoid publishing too much
            self.feedback_rate.sleep()
            distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        # Publishing the result
        navigate_end_time = rospy.get_time()
        elapsed_time = navigate_end_time - navigate_start_time
        rospy.loginfo("Navigation successful, elapsed time: " + str(elapsed_time) + " seconds")
        self.action_server.set_succeeded(Navigate2DResult(elapsed_time))



if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try :
        rospy.init_node("navigate_2D_action_server_node")

        server = Navigate2DClass()

        rospy.spin()

    except rospy.ROSInterruptException:
    	pass
