#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def movement_publisher():
    pub = rospy.Publisher('movement_command', String, queue_size=10)
    rospy.init_node('movement_publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    print("Enter commands to move the bot: forward, left, right, back. Type 'exit' to stop.")
    while not rospy.is_shutdown():
        command = input("Command: ").strip().lower()
        if command == "exit":
            break
        if command in ["forward", "left", "right", "back"]:
            rospy.loginfo(f"[Publisher] Sending command: {command}")
            pub.publish(command)
            rate.sleep()
        else:
            print("Invalid command! Use: forward, left, right, back, or exit.")

if __name__ == '__main__':
    try:
        movement_publisher()
    except rospy.ROSInterruptException:
        pass
