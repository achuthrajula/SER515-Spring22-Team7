import sys
import geometry_msgs.msg
import rclpy, termios, tty

class Controller:

    def __init__(self) -> None:
        pass
   
    def getKey(self,settings):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def controller(self):
        msg = """
        Use the following commands to control the rover
        ---------------------------
        Moving around:         
                            w, a ,s ,d to control the rover linearly
        q    w    e         q, e to increase and decrease the linear velocity of the rover              
        a    s    d         z, v to move the rover angularly
        z    x    v         x to stop the rover
                            
        CTRL-C to quit
        """

        moveBindings = {
            'w': (1, 0, 0, 0),
            'a': (1, 0, 0, 1),
            'd': (1, 0, 0, -1),
            's': (-1, 0, 0, 0),
            'j': (0, 0, 0, 1),
            'l': (0, 0, 0, -1),
            'z': (-1, 0, 0, 1),
            'v': (-1, 0, 0, -1),
        }

        speedBindings = {
            'q': (1.1, 1),
            'e': (.9, 1),
        }

        settings = termios.tcgetattr(sys.stdin)

        rclpy.init()
        node = rclpy.create_node('teleop_twist_keyboard')
        pub = node.create_publisher(geometry_msgs.msg.Twist, '/demo/cmd_demo', 10)

        speed = 1.0
        turn = 1.0
        x = 0.0
        y = 0.0
        z = 0.0
        th = 0.0
        status = 0.0

        try:
            print(msg)
            print('current speed: %s' % (speed))
            while True:
                key = self.getKey(settings)
                if key in moveBindings.keys():
                    x = moveBindings[key][0]
                    y = moveBindings[key][1]
                    z = moveBindings[key][2]
                    th = moveBindings[key][3]
                elif key in speedBindings.keys():
                    speed = speed * speedBindings[key][0]
                    turn = turn * speedBindings[key][1]
                    print('current speed: %s' % (speed))
                    if (status == 14):
                        print(msg)
                    status = (status + 1) % 15
                elif key == 'x':
                    x = 0.0
                    y = 0.0
                    z = 0.0
                    th = 0.0
                elif (key == '\x03'):
                        break

                twist = geometry_msgs.msg.Twist()
                twist.linear.x = x * speed
                twist.linear.y = y * speed
                twist.linear.z = z * speed
                twist.angular.x = 0.0
                twist.angular.y = 0.0
                twist.angular.z = th * turn
                pub.publish(twist)

        except Exception as e:
            print(e)

        finally:
            twist = geometry_msgs.msg.Twist()
            twist.linear.x = 0.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)

            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
            