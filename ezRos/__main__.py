import os
import sys
from ezRos.controller import Controller
from ezRos.test_environment import TestDrive
from ezRos.launch import Launcher
from ezRos.environment_setup import Setup
from ezRos.test_installations import Test
from ezRos.gui import GUI
from ezRos.maze_generator import MazeGenerator


def main():
    try:
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
                7. GUI
                8. Exit
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
                maze = MazeGenerator()
                maze.generate()
            elif user_input == '7':
                launch = GUI()
                launch.gui()
            elif user_input == '8':
                exit(0)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == '__main__':
    main()
