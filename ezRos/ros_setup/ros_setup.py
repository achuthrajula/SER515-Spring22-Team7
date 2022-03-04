import os
import sys

class Setup:

    def __init__(self) -> None:
        pass

    def setup(self):
        input_command = 0
        sys.path.append(os.getcwd())
        
        while input_command != "7":
            input_command = input(
                """Commands: \n
                install (i): Installs ROS2
                test (t): Tests ROS2 installation by executing a turtlsim node

                x: To exit and return to main menu
                """
            )

            if input_command == "install" or input_command == "i":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/ros2.sh")

            elif input_command == "test" or input_command == "t":
                os.system(f"sudo bash {os.getcwd()}/Installation-Scripts/test_ros2.sh")

            elif input_command == "x":
                return
