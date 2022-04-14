from ezRos.maze_generator.utils import random_number_generator_with_minimum_distance, random_number_generator


def random_maze_generator(distance, maze_spread, wall_count):
    maze_poses = {}
    # Sets x co-ordinates of the maze
    maze_poses["x"] = random_number_generator_with_minimum_distance(
        int(distance), int(maze_spread), int(wall_count))
    # Sets y co-ordinates of the maze
    maze_poses["y"] = random_number_generator_with_minimum_distance(
        int(distance), int(maze_spread), int(wall_count))
    # Sets rotation angle along z axis
    maze_poses["z"] = random_number_generator(int(wall_count))

    return maze_poses


def generate_maze(distance, maze_spread, wall_count, length):
    iterator = {}
    generated_maze = []
    maze_poses = random_maze_generator(
        distance, maze_spread, wall_count)
    maze_x = maze_poses['x']
    if maze_x == 'error':
        print('The given wall count is too high for the given area of a maze, please try again after altering the parameters')
        return 'error'
    maze_y = maze_poses['y']
    maze_z = maze_poses['z']

    z_axis_rotation = [0, 1.8]

    for i in range(len(maze_x)):
        maze = f"""<link name='Wall_{i}'>
                        <collision name='Wall_{i}_Collision'>
                            <geometry>
                            <box>
                                <size>{length} 0.15 2.5</size>
                            </box>
                            </geometry>
                            <pose>0 0 1.25 0 -0 0</pose>
                        </collision>
                        <visual name='Wall_{i}_Visual'>
                            <pose>0 0 1.25 0 -0 0</pose>
                            <geometry>
                            <box>
                                <size>{length} 0.15 2.5</size>
                            </box>
                            </geometry>
                            <material>
                            <script>
                                <uri>file://media/materials/scripts/gazebo.material</uri>
                                <name>Gazebo/Wood</name>
                            </script>
                            <ambient>1 1 1 1</ambient>
                            </material>
                            <meta>
                            <layer>0</layer>
                            </meta>
                        </visual>
                        <pose>{maze_x[i]} {maze_y[i]} 0 0 -0 {z_axis_rotation[maze_z[i]]}</pose>
                        </link>"""
        generated_maze.append(maze)

    return generated_maze
