# import statements from python's launch module

from launch import LaunchDescription
from launch_ros.actions import Node

# The launch description goes into generate_launch_description()'s return value. 
# Each Node represents a ROS node.

# As a placeholder for the launch script, we added turtlesim's nodes to the launch description. It can be updated according to the user's needs.

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    ])