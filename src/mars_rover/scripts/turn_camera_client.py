#!/usr/bin/env python3

import rospy
from mars_rover.srv import turnCamera, turnCameraResponse

from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError


if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    rospy.init_node("turn_camera_client_node")
    # this is used to interact with a service
    srv_proxy = rospy.ServiceProxy("turn_camera", turnCamera)

    user_input = input("\nAy up! Do you want to turn the camera right or left? ")

    resp_obj = srv_proxy(str(user_input))
    answer = resp_obj.answer_view
    angle = str(resp_obj.camera_angle)

    br = CvBridge()
    img = br.imgmsg_to_cv2(answer)
    cv2.namedWindow("Robot view at " + angle + " degrees", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Robot view " + angle + " degrees", img)
    # Waiting 0ms for user to press any key
    cv2.waitKey(0)
    # Using cv2.destroyAllWindows() to destroy
    # all created windows open on screen
    cv2.destroyAllWindows()

    #print("This is what you see at the angle of ", answer, "!")
