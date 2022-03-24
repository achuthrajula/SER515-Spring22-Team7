import os
from _root_path import ROOT_DIRECTORY

class Test:

    def __init__(self) -> None:
        pass

    def test(self):
        input_command = 0
        
        while input_command != "x":
            input_command = input(
                """Commands: \n
                [1]: Tests Python 3.8.10 Installation
                [2]: Tests ROS2 Installation
                [3]: Tests Gazebo Installation
                [4]: Tests Slam Installation

                x: To exit and return to main menu
                """
            )

            if input_command == "1":
                os.system(f"sudo bash {ROOT_DIRECTORY}/Installation-Scripts/python/test_python.sh")

            elif input_command == "2":
                os.system(f"sudo bash {ROOT_DIRECTORY}/Installation-Scripts/ros2/test_ros2.sh")

            elif input_command == "3":
                os.system(f"gazebo --verbose /opt/ros/foxy/share/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world")

            elif input_command == "4":
                os.system(f"sudo bash {ROOT_DIRECTORY}/Installation-Scripts/slam/slam_test.sh")

            elif input_command == "x":
                return
