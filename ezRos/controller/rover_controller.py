import os

class Controller:

    def __init__(self) -> None:
        pass

    def controller(self):
        input_command = 0

        while input_command != "x":
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

            if input_command == "w":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: 1.0}}' -1")
                speed_input = 1
                user_input = ''
                while user_input != 'c':
                    user_input = input()
                    if (user_input == "q"):
                        speed_input += 1
                        value = f'{{linear: {{x: {speed_input}}}}}'
                        os.system(
                            f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
                    elif (user_input == "e"):
                        speed_input -= 1
                        value = f'{{linear: {{x: {speed_input}}}}}'
                        os.system(
                            f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
            elif input_command == "s":
                os.system(
                    "ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: -1.0}}' -1")
                speed_input = 1
                user_input = ''
                while user_input != 'c':
                    user_input = input()
                    if (user_input == "q"):
                        speed_input += 1
                        value = f'{{linear: {{x: -{speed_input}}}}}'
                        os.system(
                            f"ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{value}' -1")
                    elif (user_input == "e"):
                        speed_input -= 1
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
