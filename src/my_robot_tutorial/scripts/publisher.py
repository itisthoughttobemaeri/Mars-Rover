import rospy
from std_msgs.msg import String

def hello_world_pub():
   # This function takes a parameter that is the name of the node
   rospy.init_node("hello_world_pub_node")
   # We publish (with a topic name) a message of type String, the queue_size are the number of messages that we can store (if exceeded, we drop the messages)
   pub = rospy.Publisher("hello_world", String, queue_size = 10)
   
   i = 0
   rate = rospy.Rate(5)
   while not rospy.is_shutdown():
     pub.publish("Hello World " + str(i))
     i+=1
     # To control the rate at which we publish, we can use the rate
     rate.sleep()

if __name__ == '__main__':
    # Unless Ros does not terminate the programm, it will run the 'try'
    try : 
    	hello_world_pub()
    except rospy.ROSInterruptException:
    	pass
