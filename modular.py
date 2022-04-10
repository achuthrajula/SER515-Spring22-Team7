from xml.etree import ElementTree as ET
from xml.dom import minidom

doc = ET.parse(
    "/home/arajula/Desktop/SER515-Spring22-Team7/Gazebo-Worlds/2_0_x_alpha_gazebo_environment.world")

# user-defined function
root = doc.getroot()

# def getNodeText(node):

#     nodelist = node.childNodes
#     result = []
#     for node in nodelist:
#         if node.nodeType == node.TEXT_NODE:
#             result.append(node.data)
#     return ''.join(result)


# links = doc.getElementsByTagName("link")

# for link in links:
#     pose = link.getElementsByTagName("pose")[0]
#     print(getNodeText(pose))


r_wheel = ET.ElementTree("link", {
    "name": "right_wheel_0"
})

r_pose = ET.SubElement(r_wheel, "pose")

r_pose.text = "0.554282 -0.625029 -0.025 -1.5707 0 0"

r_joint = ET.Element("joint", {
    "name": "right_wheel_joint_1",
    "type": "revolute"
})

l_joint = ET.Element("joint", {
    "name": "left_wheel_joint_1",
    "type": "revolute"
})

parent_r = ET.SubElement(r_joint, "parent")
parent_l = ET.SubElement(l_joint, "parent")
parent_r.text = "chassis"
parent_l.text = "chassis"

child_r = ET.SubElement(r_joint, "child")
child_r.text = "right_wheel_1"

child_l = ET.SubElement(l_joint, "child")
child_l.text = "left_wheel_1"

axis_r = ET.SubElement(r_joint, "axis")
axis_l = ET.SubElement(l_joint, "axis")

xyz_r = ET.SubElement(axis_r, "xyz")
xyz_r.text = "0 0 1"
xyz_l = ET.SubElement(axis_l, "xyz")
xyz_l.text = "0 0 1"


limit_r = ET.SubElement(axis_r, "limit")
limit_l = ET.SubElement(axis_l, "limit")

lower_r = ET.SubElement(limit_r, "lower")
lower_r.text = "-1.79769e+308"
upper_r = ET.SubElement(limit_r, "upper")
upper_r.text = "1.79769e+308"
lower_l = ET.SubElement(limit_l, "lower")
lower_l.text = "-1.79769e+308"
upper_l = ET.SubElement(limit_l, "upper")
upper_l.text = "1.79769e+308"


plugin = ET.Element("plugin", {"name": "skid_steer_drive",
                               "filename": "libgazebo_ros_diff_drive.so"})

num_wheel_pairs = ET.Element("num_wheel_pairs")
num_wheel_pairs.text = "2"

left_joint = ET.Element("left_joint")
left_joint.text = "left_wheel_joint1"

right_joint = ET.Element("right_joint")
right_joint.text = "right_wheel_joint1"

wheel_seperation = ET.Element("wheel_separation")
wheel_seperation.text = "1.25"

wheel_diameter_4_0 = ET.Element("wheel_diameter")
wheel_diameter_4_0.text = "1.0"

wheel_diameter_4_1 = ET.Element("wheel_diameter")
wheel_diameter_4_1.text = "0.6"

data1 = ET.Element("data", {"a_version": "something_v001.0002.ma",
                            "b_user": "You",
                            "c_comment": "minor save"})

root.append(r_joint)
root.append(l_joint)
# l_joint.append(parent)
# l_joint.append(child)
# l_joint.append(axis)
# axis.append(xyz)
# axis.append(limit)
# limit.append(lower)
# limit.append(upper)


out = ET.tostring(root)

dom = minidom.parseString(out)

f = open("./test.world", "wb")
f.write(out)
f.close()

print(dom.toprettyxml())
