from ezRos.controller import Controller
from ezRos.test_environment import TestDrive
from ezRos.launch import Launcher
from ezRos.ros_setup import Setup


def main():
    user_input = 0
    while(user_input != 'x'):
        user_input = input(
            """
            Choose a functionality to proceed: \n
            1. Launch testing ground
            2. Rover Controller
            3. ROS Setup
            4. Launch ROS 
            5. Exit
            """
        )
        if user_input == '1':
            launch = TestDrive()
            launch.launch()
        elif user_input == '2':
            control = Controller()
            control.controller()
        elif user_input == '3':
            setup = Setup()
            setup.setup()
        elif user_input == '4':
            launch = Launcher()
            launch.launch()
        elif user_input == '5':
            exit(0)


if __name__ == '__main__':
    main()
