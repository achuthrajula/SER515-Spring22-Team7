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
    sensor_input = input("""
        Enter the sensors for the rover\n
        [0] No Sensors
        [1] Laser
        [2] Camera
        [3] Laser and Camera
        """)
