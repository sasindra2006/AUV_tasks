#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    print("Rohan: " + data.data)

def listener():
    rospy.init_node('ros_chat_subscriber', anonymous=True)
    rospy.Subscriber('chat_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
