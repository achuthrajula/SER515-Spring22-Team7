import random


def helper(itr):
    l = []
    for _ in range(itr):
        randomnumber = random.uniform(-50, 50)
        l.append(randomnumber)

    return l


def random_number_generator_with_minimum_distance(itr):

    return [1*i + x for i, x in enumerate(random.sample(range(-25, 25), itr))]


print(random_number_generator_with_minimum_distance(20))


def random_number_generator(itr):
    l = []
    for _ in range(itr):
        l.append(random.randint(0, 1))

    return(l)


def random_obstacle_generator(obstacle_count):
    obstacle_poses = {}
    # Sets x co-ordinates of the obstacle
    obstacle_poses["x"] = random_number_generator_with_minimum_distance(
        int(obstacle_count))
    # Sets y co-ordinates of the obstacle
    obstacle_poses["y"] = random_number_generator_with_minimum_distance(
        int(obstacle_count))
    # Sets rotation angle along z axis
    obstacle_poses["z"] = random_number_generator(int(obstacle_count))

    print(obstacle_poses)
    return obstacle_poses


def generate_obstacles(obstacle_count):
    iterator = {}
    obstacles = []
    obstacles_poses = random_obstacle_generator(obstacle_count)
    obstacles_x = obstacles_poses['x']
    obstacles_y = obstacles_poses['y']
    obstacles_z = obstacles_poses['z']

    print(obstacles_x, obstacles_y, obstacles_z)
    scam = [0, 1.8]

    for i in range(len(obstacles_x)):
        obstacle = f"""<link name='Wall_{i}'>
                        <collision name='Wall_{i}_Collision'>
                            <geometry>
                            <box>
                                <size>1.5 0.15 2.5</size>
                            </box>
                            </geometry>
                            <pose>0 0 1.25 0 -0 0</pose>
                        </collision>
                        <visual name='Wall_{i}_Visual'>
                            <pose>0 0 1.25 0 -0 0</pose>
                            <geometry>
                            <box>
                                <size>1.5 0.15 2.5</size>
                            </box>
                            </geometry>
                            <material>
                            <script>
                                <uri>file://media/materials/scripts/gazebo.material</uri>
                                <name>Gazebo/Grey</name>
                            </script>
                            <ambient>1 1 1 1</ambient>
                            </material>
                            <meta>
                            <layer>0</layer>
                            </meta>
                        </visual>
                        <pose>{obstacles_x[i]} {obstacles_y[i]} 0 0 -0 {scam[obstacles_z[i]]}</pose>
                        </link>"""
        obstacles.append(obstacle)

    return obstacles
