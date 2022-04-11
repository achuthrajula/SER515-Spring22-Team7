import os
from bs4 import BeautifulSoup as bs
from ezRos.modular_assembly.utils import generate_joints, generate_plugins, generate_wheels, generate_chassis

from copy import copy
from _root_path import ROOT_DIRECTORY


class Assembler:

    def __init__(self) -> None:
        pass

    def assemble(self, val):
        if val == '2' or val == '4' or val == '6':
            print(val)
            content = []
            # Read the XML file
            with open(f"{ROOT_DIRECTORY}/Rover-Workshop/template.world", "r") as file:
                # Read each line in the file, readlines() returns a list of lines
                content = file.readlines()
                # Combine the lines in the list into a string
                content = "".join(content)
                root = bs(content, "lxml-xml")
                file.close()
                chassis = generate_chassis(val)
                wheels = generate_wheels(val)
                joints = generate_joints(val)
                print(joints)
                plugin = generate_plugins(val)
                chassis_root = bs(chassis, "lxml-xml")
                root.model.append(copy(chassis_root.link))
                for wheel in wheels:
                    wheel_root = bs(wheel, "lxml-xml")
                    root.model.append(copy(wheel_root.link))
                for joint in joints:
                    joint_root = bs(joint, "lxml")
                    root.model.append(copy(joint_root.joint))
                plugin_root = bs(plugin, "lxml")
                root.model.append(copy(plugin_root.plugin))
            with open(f'{ROOT_DIRECTORY}/Rover-Workshop/generate.xml', 'w') as f:
                f.write(str(root))

            os.system(
                f"gazebo --verbose {ROOT_DIRECTORY}/Rover-Workshop/generate.xml")

        else:
            print("Please enter a valid number of wheels")
            return
