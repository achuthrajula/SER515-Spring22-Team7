import os
from bs4 import BeautifulSoup as bs
from ezRos.modular_assembly.utils import generate_joints, generate_plugins, generate_wheels

from copy import copy
from _root_path import ROOT_DIRECTORY


class Assembler:

    def __init__(self) -> None:
        pass

    def assemble(self, val):
        if val != '2' or val != '4' or val != '6':
            print("Please enter a valid number of wheels")
            return

        else:
            content = []
            # Read the XML file
            with open(f"{ROOT_DIRECTORY}/Rover-Workshop/template.world", "r") as file:
                # Read each line in the file, readlines() returns a list of lines
                content = file.readlines()
                # Combine the lines in the list into a string
                content = "".join(content)
                root = bs(content, "lxml-xml")
                file.close()
                wheels = generate_wheels(val)
                joints = generate_joints(val)
                plugin = generate_plugins(val)
                for wheel in wheels:
                    wheel_root = bs(wheel, "lxml-xml")
                    root.model.append(copy(wheel_root.link))
                for joint in joints:
                    content = joint
                    joint_root = bs(content, "lxml")
                    root.model.append(copy(joint_root.joint))
                content = plugin
                plugin_root = bs(content, "lxml")
                root.model.append(copy(plugin_root.plugin))
                plugin_root = bs(content, "lxml")
            with open(f'{ROOT_DIRECTORY}/Rover-Workshop/generate.xml', 'w') as f:
                f.write(str(root))
            os.system(
                f"gazebo --verbose {ROOT_DIRECTORY}/Rover-Workshop/generate.xml")
