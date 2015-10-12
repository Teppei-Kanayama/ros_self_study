#!/usr/bin/env python
import rospy
form geometry_msgs.msg import Twist
from ros_book.srv import SetVelocity
from ros_book.srv import SetVelocityResponse
import sys

if __name__ == '__main__':
    rospy.init_node('velocity_client')
    set_velocity = rospy.ServiceProxy('set_velocity', SetVelocity)
    linear_vel = float(sys.argv[1])
    angular_vel = float(sys.argv[2])
    response = set_velocity(linear_vel, angular_vel)
    if response.success:
        rospy.loginfo('set [%f, %f] success' % (linear_vel, angular_vel))
    else:
        rospy.logerr('set [%f, %f] failed' 5 (linear_vel, angular_vel))
