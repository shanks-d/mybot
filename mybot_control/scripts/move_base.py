#!/usr/bin/env python

###################################################################################################################
# CODE TO DRIVE THE ROBOT VIA TELEOPERATION
# PRESS 'w' TO MOVE FORWARD
# PRESS 's' TO MOVE BACKWARD
# PRESS 'i' TO INCREMENT SPEED BY 0.5
# PRESS 'J' TO DECREMENT SPEED BY 0.5
# PRESS 'k' TO RESET SPEED TO 0
###################################################################################################################

import rospy
from std_msgs.msg import Float64, String
from geometry_msgs.msg import Twist
import math

speed = 0.0

def callback(key): 
    global speed
    if key.data == '':
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
    elif key.data == 'i':
        speed += 0.05
        if speed > 10.0:
            speed = 10.0
    elif key.data == 'j':
        speed -= 0.05
        if speed < -10.0:
            speed = -10.0
    elif key.data == 'k':
        speed = 0.0
    elif key.data == 'w':
        vel_msg.linear.x = speed
        vel_msg.angular.z = 0.0
    elif key.data == 's':
        vel_msg.linear.x = (-1)*speed
        vel_msg.angular.z = 0.0
    elif key.data == 'a':
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 2.0
    elif key.data == 'd':
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = -2.0
    print "Key: ", key.data, "Speed: ", speed

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    try:
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/teleop_key',String,callback)
        vel_msg = Twist()
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            velocity_publisher.publish(vel_msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
