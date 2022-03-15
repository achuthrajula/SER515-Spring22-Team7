import os
import sys

class TestDrive:

    def __init__(self) -> None:
        pass

    def launch(self):
        wheel_input = input('Enter the number of wheels for the rover\n')
        sys.path.append(os.getcwd())

        os.system(f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/{wheel_input}x_alpha_gazebo_environment.world")
