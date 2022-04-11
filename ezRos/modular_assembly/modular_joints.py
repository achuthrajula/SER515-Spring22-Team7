
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
        'name': 'right_wheel_joint_1',
        'child': 'right_wheel_1',
    },
}

joint_generator_2x = {
    'left_wheel_joint': {
        'name': 'left_wheel_joint',
        'child': 'left_wheel',
    },
    'right_wheel_joint': {
        'name': 'right_wheel_joint',
        'child': 'right_wheel',
    }
}


def generate_joints(joint_count):
    iterator = {}
    joints = []
    if joint_count == '4':
        iterator = joint_generator_4x
    elif joint_count == '2':
        iterator = joint_generator_2x

    for key, value in iterator.items():
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

    return joints
