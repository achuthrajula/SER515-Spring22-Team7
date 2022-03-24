import os
from _root_path import ROOT_DIRECTORY

class Launcher:

    def __init__(self) -> None:
        pass

    def launch(self):
        os.system(f"ros2 launch {ROOT_DIRECTORY}/ezRos/launch/launch.py")
