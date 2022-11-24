#! /usr/bin/python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def movebase_client():
    client = actionlib.SimpleActionClient('move_basse'. MoveBaseAction)
    client.wait_fot_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 0.5
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    wait =client.wait_for_result()

    if not wait:
        rospy.logerr('Action server not availab')
        rospy.signal_shutdown("podu ambutu then")
    else:
        return client.get_result()


if __name__ == '__main__' :
    try:
        rospy.init_node('drive_bot')
        result = movebase_client()
        if result:
            rospy.loginfo("goal execution done!!")
    except rospy.ROSInterruptException:
        rospy.loginfo("done ehhhhhh")
