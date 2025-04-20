#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node("publisher_node")
    pub = rospy.Publisher("/input", Int32, queue_size=10)
    rate = rospy.Rate(1)

    value = 2
    while not rospy.is_shutdown():
        rospy.loginfo(f"[Publisher] Sending: {value}")
        pub.publish(value)
        value += 2
        rate.sleep()

if __name__ == "__main__":
    main()
