#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    final = msg.data + 5
    rospy.loginfo(f"[Adder] Final Result: {final}")

if __name__ == "__main__":
    rospy.init_node("adder_node")
    rospy.Subscriber("/intermediate", Int32, callback)
    rospy.spin()
