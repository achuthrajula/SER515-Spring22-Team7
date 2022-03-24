import os
from _root_path import ROOT_DIRECTORY

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
            """
        )

        #os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/{wheel_input}x_alpha_gazebo_environment.world")
        os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/{wheel_input}_{sensor_input}_x_alpha_gazebo_environment.world")

    def generateMaze(self):
        os.system(f"gazebo --verbose {ROOT_DIRECTORY}/Gazebo-Worlds/Maze.world")
