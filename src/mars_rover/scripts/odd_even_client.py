#!/usr/bin/env python3

import rospy
from mars_rover.srv import oddEvenCheck, oddEvenCheckResponse



if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    rospy.init_node("odd_even_client_node")
    # this is used to interact with a service
    srv_proxy = rospy.ServiceProxy("odd_even_check", oddEvenCheck)
    
    user_input = input("\nAy up! Enter a whole number: ")
    
    resp_obj = srv_proxy(int(user_input))
    answer = resp_obj.answer
    
    print("The number you choose is", answer, "!")
