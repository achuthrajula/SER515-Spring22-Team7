import os
import sys

input_command = 0
while input_command != "7":
    input_command = input(
        """Commands: \n
        1. To open gazebo with the motor model\n
        2. To Move the motor forward\n
        3. To Move the motor backward\n
        4. To Stop the motor\n
        5. To rotate the motor counter-clockwise\n
        6. To rotate the motor clockwise\n
        7. To exit\n"""
    )


    if input_command == "1":
        os.system(
            "gazebo --verbose /opt/ros/foxy/share/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world")
    elif input_command == "2":
        os.system(
            "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: 1.0}}' -1")
        speed_input = 1
        while speed_input != 0:
                speed_input = float(input("Pick a value from 1 to 9 to set the speed and enter 0 to exit loop \n"))
                if (speed_input >= 1.0 and speed_input <= 9.0):
                    value = f'{{linear: {{x: {speed_input}}}}}'
                    os.system(
                    f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
    elif input_command == "3":
        os.system(
            "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: -1.0}}' -1")
        speed_input = 1
        while speed_input != 0:
                speed_input = float(input("Pick a value from -1 to -9 to set the speed and enter 0 to exit loop \n"))
                if (speed_input >= -9.0 and speed_input <= -1.0):
                    value = f'{{linear: {{x: {speed_input}}}}}'
                    os.system(
                    f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
    elif input_command == "4":
        os.system(
            "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: 0.0}}' -1")
    elif input_command == "5":
        os.system(
            "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{angular: {z: 1.0}}' -1")
    elif input_command == "6":
        os.system(
            "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{angular: {z: -1.0}}' -1")
    elif input_command == "7":
        sys.exit()
