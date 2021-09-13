#!/usr/bin/env python 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def __init__(self):
    rospy.init_node('turtlebot_controller', anonymous=True)

    self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    self.pose_subscriber = rospy.Subcriber('/turtle1/pose', Pose, self.update_pose)
    self.pose= Pose()
    sefl.rate = rospy.Rate(10)

def update_pose(self, data):
    self.pose = data
    self.pose.x = round(self.pose.x, 4)
    self.pose.y = round(self.pose.y, 4)

    rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()


