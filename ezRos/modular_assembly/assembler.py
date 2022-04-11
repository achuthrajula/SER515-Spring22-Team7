from lib2to3.pgen2.tokenize import generate_tokens
from bs4 import BeautifulSoup as bs
from ezRos.modular_assembly.utils import generate_joints, generate_plugins, generate_wheels

from copy import copy
from _root_path import ROOT_DIRECTORY

content = []
# Read the XML file
with open(f"{ROOT_DIRECTORY}/template.world", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    root = bs(content, "lxml-xml")
    result = root.find("model")
    # print(result)
    file.close()
    wheels = generate_wheels(4)
    joints = generate_joints(4)
    plugin = generate_plugins(4)
    for wheel in wheels:
        content = wheel
        wheel_root = bs(content, "lxml-xml")
        print(wheel_root)
        root.model.append(copy(wheel_root.link))
    for joint in joints:
        content = joint
        joint_root = bs(content, "lxml")
        root.model.append(copy(joint_root.joint))
    content = plugin
    plugin_root = bs(content, "lxml")
    root.model.append(copy(plugin_root.plugin))
    plugin_root = bs(content, "lxml")
with open('./test.xml', 'w') as f:
    f.write(str(root))
