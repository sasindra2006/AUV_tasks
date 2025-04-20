#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from task_3.msg import bot_pose

class BotMovement:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = "north"
        self.sub = rospy.Subscriber('movement_command', String, self.callback)
        self.pub = rospy.Publisher('bot_position', bot_pose, queue_size=10)

    def callback(self, msg):
        command = msg.data
        if command == "forward":
            if self.facing == "north":
                self.y += 1
            elif self.facing == "south":
                self.y -= 1
            elif self.facing == "east":
                self.x += 1
            elif self.facing == "west":
                self.x -= 1
        elif command == "back":
            if self.facing == "north":
                self.y -= 1
            elif self.facing == "south":
                self.y += 1
            elif self.facing == "east":
                self.x -= 1
            elif self.facing == "west":
                self.x += 1
        elif command == "left":
            if self.facing == "north":
                self.facing = "west"
            elif self.facing == "west":
                self.facing = "south"
            elif self.facing == "south":
                self.facing = "east"
            elif self.facing == "east":
                self.facing = "north"
        elif command == "right":
            if self.facing == "north":
                self.facing = "east"
            elif self.facing == "east":
                self.facing = "south"
            elif self.facing == "south":
                self.facing = "west"
            elif self.facing == "west":
                self.facing = "north"

        # Publish the updated position
        bot_position = bot_pose()
        bot_position.x = self.x
        bot_position.y = self.y
        bot_position.facing = self.facing
        self.pub.publish(bot_position)
        rospy.loginfo(f"[Subscriber] Bot Position: {self.x}, {self.y}, {self.facing}")

def bot_movement_listener():
    rospy.init_node('bot_subscriber', anonymous=True)
    bot_movement = BotMovement()
    rospy.spin()

if __name__ == '__main__':
    bot_movement_listener()
