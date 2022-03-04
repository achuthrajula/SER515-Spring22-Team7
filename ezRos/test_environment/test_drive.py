import os
import sys

class TestDrive:

    def __init__(self) -> None:
        pass

    def launch(self):
        sys.path.append(os.getcwd())

        os.system(f"gazebo --verbose {os.getcwd()}/Gazebo-Worlds/test.world")
