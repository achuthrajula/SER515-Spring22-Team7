from ezRos.controller import Controller
from ezRos.test_launch import TestDrive
import launch

def main():
    user_input = 0
    while(user_input != 'x'):
        user_input = input(
            """
            Choose a functionality to proceed: \n
            1. Launch testing ground
            2. Rover Controller
            3. foo
            """
        )
        if user_input == '1':
            launch = TestDrive()
            launch.launch()
        elif user_input == '2':
            control = Controller()
            control.controller()
    
if __name__ == '__main__':
    main()

