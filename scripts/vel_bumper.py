#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

rospy.init_node('vel_bumper')
vel_x = rospy.get_param('~vel_x', 0.5)
vel_rot = rospy.get_param('~vel_rot', 1.0)
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 1)

def callback(bumper):
    print bumper
    vel = Twist()
    vel.linear.x = -1.0
    pub.publish(vel)

sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback)

while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input('f, b, l, r, q: ')
    if 'f' in direction:
        vel.linear.x = vel_x
    if 'b' in direction:
        vel.linear.x = vel_x * (-1)
    if 'l' in direction:
        vel.angular.z = vel_rot
    if 'r' in direction:
        vel.angular.z = vel_rot * (-1)
    if 'q' in direction:
        break
    print vel
    pub.publish(vel)
