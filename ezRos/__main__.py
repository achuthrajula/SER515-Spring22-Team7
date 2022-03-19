from cgitb import handler
from ezRos.controller import Controller
from ezRos.test_environment import TestDrive
from ezRos.launch import Launcher
from ezRos.environment_setup import Setup
from ezRos.test_installations import Test

def main():
    user_input = 0
    while(user_input != 'x'):
        user_input = input(
            """
            Choose a functionality to proceed: \n
            1. Launch testing ground
            2. Rover Controller
            3. Environment Setup
            4. Test Installations
            5. Launch ROS 
            6. Generate Maze
            7. Exit
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
            test = Test()
            test.test()
        elif user_input == '5':
            launch = Launcher()
            launch.launch()
        elif user_input == '6':
            launch = TestDrive()
            launch.generateMaze()
        elif user_input == '7':
            exit(0)


if __name__ == '__main__':
    main()
