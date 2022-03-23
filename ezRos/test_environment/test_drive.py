import os
import sys

class TestDrive:

    def __init__(self) -> None:
        pass

    def launch(self):
        wheel_input = input('Enter the number of wheels for the rover\n')

        sensor_input = input(
            """
            Enter the sensors you want mounted: \n
            0. No sensors
            1. LASER
            2. Camera
            3. Camera and LASER
            """
        )
        sys.path.append(os.getcwd())

        os.system(f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/{wheel_input}_{sensor_input}_x_alpha_gazebo_environment.world")

    def generateMaze(self):
        os.system(f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/Maze.world")
