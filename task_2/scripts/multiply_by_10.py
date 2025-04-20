#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    result = msg.data * 10
    rospy.loginfo(f"[Multiplier] Received {msg.data}, sending {result}")
    pub.publish(result)

if __name__ == "__main__":
    rospy.init_node("multiplier_node")
    pub = rospy.Publisher("/intermediate", Int32, queue_size=10)
    rospy.Subscriber("/input", Int32, callback)
    rospy.spin()
