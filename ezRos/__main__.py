from ezRos.controller import Controller

def main():
    user_input = 0
    while(user_input != 'x'):
        user_input = input(
            """
            Choose a functionality to proceed: \n
            1. Rover Controller
            2. foo
            3. foo
            """
        )
        if user_input == '1':
            controller = Controller()
            controller.controller()
    
if __name__ == '__main__':
    main()

