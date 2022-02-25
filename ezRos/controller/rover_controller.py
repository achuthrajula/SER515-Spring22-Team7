import os
import sys

class Controller:

    def __init__(self) -> None:
        pass

    def controller(self):
        input_command = 0
        sys.path.append(os.getcwd())

        while input_command != "7":
            input_command = input(
                """Commands: \n
                K to start the rover
                Use the following numbers to control the rover: \n
                                Q & E to (+/-) velocity
                   W            C to exit velocity control
                A  S  D         R to stop rover
                                X to exit program
                """
            )

            if input_command == "k":
                os.system(
                    f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/alpha_gazebo_environment.world")
            elif input_command == "w":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: 1.0}}' -1")
                speed_input = 1
                while speed_input != 0:
                    speed_input = float(
                        input("Input 1 to 9 to set velocity and 0 to return to controller \n"))
                    if (speed_input >= 1.0 and speed_input <= 9.0):
                        value = f'{{linear: {{x: {speed_input}}}}}'
                        os.system(
                            f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
            elif input_command == "s":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: -1.0}}' -1")
                speed_input = 1
                while speed_input != 0:
                    speed_input = float(
                        input("Input 1 to 9 to set velocity and 0 to return to controller \n"))
                    if (speed_input >= 1.0 and speed_input <= 9.0):
                        value = f'{{linear: {{x: -{speed_input}}}}}'
                        os.system(
                            f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
            elif input_command == "r":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: 0.0}}' -1")
            elif input_command == "a":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{angular: {z: 1.0}}' -1")
            elif input_command == "d":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{angular: {z: -1.0}}' -1")
            elif input_command == "x":
                return
