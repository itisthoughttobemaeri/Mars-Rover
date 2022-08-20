#!/usr/bin/env python3

import rospy
from mars_rover.srv import oddEvenCheck, oddEvenCheckResponse

def check_number(req):
   # Check if the number is even or odd
   # We call req.number because we defined it in the service
   if (req.number % 2) == 0:
   	check = "even"
   else:
   	check = "odd"
   # even = 0, odd = 1
   return oddEvenCheckResponse(check)  

if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try : 
    	rospy.init_node("odd_even_service_node")
    	# Create the service, giving the service and the callback function
    	rospy.Service("odd_even_check", oddEvenCheck, check_number)
    	rospy.spin()
    	
    except rospy.ROSInterruptException:
    	pass
