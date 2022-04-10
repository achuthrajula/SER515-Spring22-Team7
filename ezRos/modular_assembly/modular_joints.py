from xml.etree import ElementTree as ET
from xml.dom import minidom

joint_generator_4x = {
    'left_wheel_joint_0': {
        'name': 'left_wheel_joint_0',
        'child': 'left_wheel_0',
    },
    'right_wheel_joint_0': {
        'name': 'right_wheel_joint_0',
        'child': 'right_wheel_0',
    },
    'left_wheel_joint_1': {
        'name': 'left_wheel_joint_1',
        'child': 'left_wheel_1',
    },
    'right_wheel_joint_1': {
        'name': 'left_wheel_joint_1',
        'child': 'left_wheel_1',
    },
}

joint_generator_2x = {
    'left_wheel_joint': {
        'name': 'left_wheel_joint',
        'child': 'left_wheel',
    },
    'right_wheel_joint': {
        'name': 'right_wheel_joint',
        'child': '0.554282 -0.625029 -0.025 -1.5707 0 0',
    }
}

joints = []

for key, value in joint_generator_2x.items():
    print(value)
    joint = f"""<joint name='{value['name']}' type='revolute'>
          <parent>chassis</parent>
          <child>{value['child']}</child>
          <axis>
            <xyz>0 0 1</xyz>
            <limit>
              <lower>-1.79769e+308</lower>
              <upper>1.79769e+308</upper>
            </limit>
          </axis>
        </joint>"""
    joints.append(joint)

for joint in joints:
    data = minidom.parseString(joint)

    print(data.toprettyxml())
