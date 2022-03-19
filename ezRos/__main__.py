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
            2. Launch Maze
            3. Rover Controller
            4. ROS Setup
            5. Launch ROS 
            6. Exit
            """
        )
        if user_input == '1':
            launch = TestDrive()
            launch.launch()
        elif user_input == '2':
            launch = TestDrive()
            launch.generateMaze()
        elif user_input == '3':
            control = Controller()
            control.controller()
        elif user_input == '4':
            setup = Setup()
            setup.setup()
        elif user_input == '5':
            launch = Launcher()
            launch.launch()
        elif user_input == '6':
            exit(0)


if __name__ == '__main__':
    main()
