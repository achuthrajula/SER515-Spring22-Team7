def generate_boundary(maze_spread):
    iterator = {}
    wall_names = ['boundary_1', 'boundary_2', 'boundary_3', 'boundary_4']
    generated_maze = []
    maze_y = [int(maze_spread)*2, -int(maze_spread)*2, 0, 0]
    maze_x = [0, 0, int(maze_spread)*2, -int(maze_spread)*2]
    orientation = [0, 0, 1.57, 1.57]
    if maze_x == 'error':
        print('The given wall count is too high for the given area of a maze, please try again after altering the parameters')
        return 'error'

    z_axis_rotation = [0, 1.57]

    for i in range(len(maze_x)):
        maze = f"""<link name='{wall_names[i]}'>
                        <collision name='{wall_names[i]}_Collision'>
                            <geometry>
                            <box>
                                <size>{int(maze_spread)*4} 0.15 2.5</size>
                            </box>
                            </geometry>
                            <pose>0 0 1.25 0 -0 0</pose>
                        </collision>
                        <visual name='{wall_names[i]}_Visual'>
                            <pose>0 0 1.25 0 -0 0</pose>
                            <geometry>
                            <box>
                                <size>{int(maze_spread)*4} 0.15 2.5</size>
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
                        <pose>{maze_x[i]} {maze_y[i]} 0 0 -0 {orientation[i]}</pose>
                        </link>"""
        generated_maze.append(maze)

    return generated_maze
