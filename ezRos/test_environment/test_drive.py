import os
import sys

class TestDrive:

    def __init__(self) -> None:
        pass

    def launch(self):
        wheel_input = input('Enter the number of wheels for the rover\n')

        sensor_input = input(
            """
            Choose the sensors you want mounted: \n
            0. No Sensor
            1. LASER
            """
        )
        

        sys.path.append(os.getcwd())

        os.system(f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/{wheel_input}_{sensor_input}_x_alpha_gazebo_environment.world")
        #os.system(f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/{wheel_input}x_alpha_gazebo_environment.world")
