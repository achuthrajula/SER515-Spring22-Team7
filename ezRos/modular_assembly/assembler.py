from bs4 import BeautifulSoup as bs
from ezRos.modular_assembly.modular_joints import generate_joints
from copy import copy

content = []
# Read the XML file
with open("/home/arajula/Desktop/SER515-Spring22-Team7/template.world", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    root = bs(content, "lxml-xml")
    print(root)
    result = root.find("model")
    # print(result)
    file.close()
    joints = generate_joints(2)
    for joint in joints:
        content = joint
        joint_root = bs(content, "lxml")
        root.model.append(copy(joint_root.joint))
    joint_root = bs(content, "lxml")
    root.model.append(copy(joint_root.joint))
with open('./test.xml', 'w') as f:
    f.write(str(root))
