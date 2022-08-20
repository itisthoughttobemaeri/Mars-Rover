#!/usr/bin/env python3

import rospy
#import rospkg

from mars_rover.srv import turnCamera, turnCameraResponse

from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError

def turn_camera(req):
   # Check if the requested direction is left or right
   # We call req.direction because we defined it in the service
   current_camera_angle = rospy.get_param("/camera_angle")
   if (req.direction == 'right'):
       # The camera can't turn more right than 30 degrees
       if (current_camera_angle != 30):
           # The camera turns 15 degrees by default
   	       current_camera_angle += 15
   else:
       	# The camera can't turn more left than -15 degrees
        if (current_camera_angle != -30):
            # The camera turns 15 degrees by default
            current_camera_angle -= 15
   rospy.set_param("/camera_angle", current_camera_angle)

   #rospack = rospkg.RosPack()
   image_path = '/home/mari/catkin_ws/src/mars_rover/scripts/'
   img = cv2.imread(image_path + str(current_camera_angle) + '.png')

   br = CvBridge()
   img_msg = br.cv2_to_imgmsg(img)
   return turnCameraResponse(img_msg, current_camera_angle)

if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try :
        rospy.set_param("/camera_angle", 0)
        rospy.init_node("turn_camera_service_node")
    	# Create the service, giving the service and the callback function
        rospy.Service("turn_camera", turnCamera, turn_camera)
        rospy.spin()

    except rospy.ROSInterruptException:
    	pass
