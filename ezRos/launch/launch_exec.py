import os

class Launcher:

    def __init__(self) -> None:
        pass

    def launch(self):
        os.system(f"ros2 launch {os.getcwd()}/ezRos/launch/launch.py")
