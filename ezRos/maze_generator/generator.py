import os
from bs4 import BeautifulSoup as bs
from alive_progress import alive_bar
import time
from ezRos.maze_generator.utils import generate_obstacles
from copy import copy
from _root_path import ROOT_DIRECTORY


class MazeGenerator:

    def __init__(self) -> None:
        pass

    def generate(self):
        user_requirement = input("""
        [O] for Random Obstacle Generation
        """)
        distance_between = 1
        if (user_requirement == 'o'):
            maze_spread = input(
                'Enter the spread area of obstacles: [Suggested: 25-100] \n')
            number_of_obstacles = input(
                'Enter the number of obstacles to be generated [Suggested: 50-100]\n')
            distance_between = input(
                'Enter the minimum distance between the obstacles [Suggested: 1-3] \n')

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
            obstacles = generate_obstacles(
                distance_between, maze_spread, number_of_obstacles)
            if obstacles == 'error':
                return
            for obstacle in obstacles:
                obstacles_root = bs(obstacle, "lxml-xml")
                root.model.append(copy(obstacles_root.link))

        with open(f'{ROOT_DIRECTORY}/Maze-Workshop/Obstacles/model.sdf', 'w') as f:
            f.write(str(root))

        os.system(
            f"gazebo")
