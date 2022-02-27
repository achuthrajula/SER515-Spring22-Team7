from ezRos.controller import Controller
from ezRos.test_environment import TestDrive
from ezRos.launch import Launcher

def main():
    user_input = 0
    while(user_input != 'x'):
        user_input = input(
            """
            Choose a functionality to proceed: \n
            1. Launch testing ground
            2. Rover Controller
            3. Launch ROS 
            """
        )
        if user_input == '1':
            launch = TestDrive()
            launch.launch()
        elif user_input == '2':
            control = Controller()
            control.controller()
        elif user_input == '3':
            launch = Launcher()
            launch.launch()
    
if __name__ == '__main__':
    main()

