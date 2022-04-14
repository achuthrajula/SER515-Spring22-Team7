wheel_generator_8x = {
    'left_wheel_0': {
        'name': 'left_wheel_0',
        'pose': '1.394283 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_0': {
        'name': 'right_wheel_0',
        'pose': '1.394282 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'left_wheel_1': {
        'name': 'left_wheel_1',
        'pose': '0.262862 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_1': {
        'name': 'right_wheel_1',
        'pose': '0.262862 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'left_wheel_2': {
        'name': 'left_wheel_2',
        'pose': '-0.957138 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_2': {
        'name': 'right_wheel_2',
        'pose': '-0.957138 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'left_wheel_3': {
        'name': 'left_wheel_3',
        'pose': '-2.177138 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_3': {
        'name': 'right_wheel_3',
        'pose': '-2.177138 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
}

wheel_generator_6x = {
    'left_wheel_0': {
        'name': 'left_wheel_0',
        'pose': '0.994283 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_0': {
        'name': 'right_wheel_0',
        'pose': '0.994282 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'left_wheel_1': {
        'name': 'left_wheel_1',
        'pose': '-0.137138 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_1': {
        'name': 'right_wheel_1',
        'pose': '-0.137138 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'left_wheel_2': {
        'name': 'left_wheel_2',
        'pose': '-1.357138 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_2': {
        'name': 'right_wheel_2',
        'pose': '-1.357138 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
}

wheel_generator_4x = {
    'left_wheel_0': {
        'name': 'left_wheel_0',
        'pose': '0.554283 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.5,
    },
    'right_wheel_0': {
        'name': 'right_wheel_0',
        'pose': '0.554282 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.5,
    },
    'left_wheel_1': {
        'name': 'left_wheel_1',
        'pose': '-0.554283 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel_1': {
        'name': 'right_wheel_1',
        'pose': '-0.554282 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    }
}

wheel_generator_2x = {
    'left_wheel': {
        'name': 'left_wheel',
        'pose': '0.554283 0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    },
    'right_wheel': {
        'name': 'right_wheel',
        'pose': '0.554282 -0.625029 -0.025 -1.5707 0 0',
        'radius': 0.3,
    }
}


def generate_wheels(wheel_count):
    iterator = {}
    wheels = []
    if wheel_count == '8':
        iterator = wheel_generator_8x
    elif wheel_count == '6':
        iterator = wheel_generator_6x
    elif wheel_count == '4':
        iterator = wheel_generator_4x
    elif wheel_count == '2':
        iterator = wheel_generator_2x

    for key, value in iterator.items():
        wheel = f"""<link name='{value['name']}'>
                <pose>{value['pose']}</pose>
                <inertial>
                    <mass>2</mass>
                    <inertia>
                    <ixx>0.145833</ixx>
                    <ixy>0</ixy>
                    <ixz>0</ixz>
                    <iyy>0.145833</iyy>
                    <iyz>0</iyz>
                    <izz>0.125</izz>
                    </inertia>
                </inertial>
                <visual name='visual'>
                <material>
                    <!-- Wheel material -->
                    <ambient>0.1 0.1 0.1 1</ambient>
                    <diffuse>0.1 0.1 0.2 1</diffuse>
                    <specular>0 0 0 0</specular>
                    <emissive>0 0 0 1</emissive>
                </material> <!-- End wheel material -->
                    <geometry>
                    <sphere>
                        <radius>{value['radius']}</radius>
                    </sphere>
                    </geometry>
                </visual>
                <collision name='collision'>
                    <geometry>
                    <sphere>
                        <radius>{value['radius']}</radius>
                    </sphere>
                    </geometry>
                    <surface>
                    <friction>
                        <ode>
                        <mu>1</mu>
                        <mu2>1</mu2>
                        <slip1>0</slip1>
                        <slip2>0</slip2>
                        </ode>
                    </friction>
                    <contact>
                        <ode>
                        <soft_cfm>0</soft_cfm>
                        <soft_erp>0.2</soft_erp>
                        <kp>1e+13</kp>
                        <kd>1</kd>
                        <max_vel>0.01</max_vel>
                        <min_depth>0.01</min_depth>
                        </ode>
                    </contact>
                    </surface>
                </collision>
                </link>"""
        wheels.append(wheel)

    return wheels
