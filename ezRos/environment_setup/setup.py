import os
import sys

class Setup:

    def __init__(self) -> None:
        pass

    def setup(self):
        input_command = 0
        sys.path.append(os.getcwd())
        
        while input_command != "x":
            input_command = input(
                """Commands: \n
                [1]: Installs Python 3.8.10
                [2]: Installs ROS2
                [3]: Installs Gazebo
                [4]: Installs Slam
                [5]: Installs Rviz

                x: To exit and return to main menu
                """
            )

            if input_command == "1":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/python/python.sh")

            elif input_command == "2":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/ros2/ros2.sh")

            elif input_command == "3":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/gazebo/gazebo.sh")

            elif input_command == "4":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/slam/SLAM.sh")

            elif input_command == "5":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/rviz2/rviz2.sh")

            elif input_command == "x":
                return
