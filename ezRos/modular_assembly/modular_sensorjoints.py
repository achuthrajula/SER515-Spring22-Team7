joint_generator = {
    'laser': {
        'name': 'laser_joint',
        'child': 'laser_link',
    },
    'camera':{
        'name': 'camera_joint',
        'child': 'camera_link',
    },
}


def generate_sensorjoints(req_sensors):
    iterator = []
    sensorjoints = []
    if not req_sensors:
        return []
    elif 'laser' in req_sensors and 'camera' not in req_sensors:
        iterator.append('laser')
    elif 'laser' not in req_sensors and 'camera' in req_sensors:
        iterator.append('camera')
    elif 'laser' in req_sensors and 'camera' in req_sensors:
        iterator.extend(['laser','camera'])

    for value in iterator:
        data = joint_generator[value]
        joint = f"""<joint name='{data['name']}' type='revolute'>
            <parent>chassis</parent>
            <child>{data['child']}</child>
            </joint>"""
        sensorjoints.append(joint)
    return sensorjoints