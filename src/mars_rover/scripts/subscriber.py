#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def rpm_to_ms(wheel_size, rpm):
    return 0.1047*float(wheel_size)*float(str(rpm))

def process_rpm_msg(data):
    # wheel radius expressed in meters  
    wheel_radius = rospy.get_param("/wheel_radius_mt")
    rpm = data.data
    speed = rpm_to_ms(wheel_radius, rpm)
    message = "Message received " + str(rpm) + " , speed: " + str(speed) + " m/s"
    print(message)
    publish("/speed", speed, Float32, 10)
    
def publish(topic, msg, msg_type, queue_size):
    pub = rospy.Publisher(topic, msg_type, queue_size = queue_size)
    pub.publish(msg)
    
def create_subscriber():
    rospy.init_node("rpm_sensor_sub_node")
    # It takes the name of the topic, a message type and the callback function
    rospy.Subscriber("/rpm", Float32, process_rpm_msg)

if __name__ == '__main__':
    create_subscriber()
    # This function prevent the script from closing
    rospy.spin()
