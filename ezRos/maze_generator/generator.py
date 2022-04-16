import os
from bs4 import BeautifulSoup as bs
from alive_progress import alive_bar
import time
from ezRos.maze_generator.random_obstacles_generator import generate_obstacles
from ezRos.maze_generator.random_maze_generator import generate_maze
from ezRos.maze_generator.maze_boundary_generator import generate_boundary
from copy import copy
from _root_path import ROOT_DIRECTORY


class MazeGenerator:

    def __init__(self) -> None:
        pass

    def generate(self):
        user_requirement = input("""
        [O] for Random Obstacle Generation
        [M] for Random Maze Generation
        """)
        distance_between = 1
        length = 20
        if (user_requirement == 'o' or user_requirement == 'O'):
            maze_spread = input(
                'Enter the spread area of obstacles: [Suggested: 25-100] \n')
            number_of_obstacles = input(
                'Enter the number of obstacles to be generated [Suggested: 50-100]\n')
            distance_between = input(
                'Enter the minimum distance between the obstacles [Suggested: 1-3] \n')

        elif(user_requirement == 'm' or user_requirement == 'M'):
            maze_spread = input(
                'Enter the spread area of the maze: [Suggested: 25-50] \n')
            number_of_walls = input(
                'Enter the number of walls to be generated [Suggested: 25-40]\n')
            distance_between = input(
                'Enter the minimum distance between the walls [Suggested: 2-4] \n')
            length = input(
                'Enter the length of the walls [Suggested: 20-30] \n')

        else:
            return

        print('A random maze is being generated using ;)\n')
        with alive_bar(100, ctrl_c=False, title=f'Generating maze ... ') as bar:
            for _ in range(100):
                time.sleep(0.015)
                bar()

        content = []
        # Read the XML file
        with open(f"{ROOT_DIRECTORY}/Maze-Workshop/template.xml", "r") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.readlines()
            # Combine the lines in the list into a string
            content = "".join(content)
            root = bs(content, "lxml-xml")
            file.close()
            if user_requirement == 'o' or user_requirement == 'O':
                obstacles = generate_obstacles(
                    distance_between, maze_spread, number_of_obstacles)
                if obstacles == 'error':
                    return
                for obstacle in obstacles:
                    obstacles_root = bs(obstacle, "lxml-xml")
                    root.model.append(copy(obstacles_root.link))

                with open(f'{ROOT_DIRECTORY}/Maze-Workshop/Obstacles/model.sdf', 'w') as f:
                    f.write(str(root))

            if user_requirement == 'm' or user_requirement == 'M':
                maze = generate_maze(
                    distance_between, maze_spread, number_of_walls, length)
                if maze == 'error':
                    return
                for wall in maze:
                    wall_root = bs(wall, "lxml-xml")
                    root.model.append(copy(wall_root.link))
                boundary = generate_boundary(maze_spread)
                for wall in boundary:
                    wall_root = bs(wall, "lxml-xml")
                    root.model.append(copy(wall_root.link))

                with open(f'{ROOT_DIRECTORY}/Maze-Workshop/Maze/model.sdf', 'w') as f:
                    f.write(str(root))

        os.system(
            f"gazebo")
