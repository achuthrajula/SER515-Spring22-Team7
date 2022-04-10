from xml.etree import ElementTree as ET
from xml.dom import minidom

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
        'pose': '0.554282 0.625029 -0.025 -1.5707 0 0',
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

wheels = []

for key, value in wheel_generator_2x.items():
    wheel = f"""<link name="{value['name']}">
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

for wheel in wheels:
    # print(wheel)
    data = minidom.parseString(wheel)

    print(data.toprettyxml())
