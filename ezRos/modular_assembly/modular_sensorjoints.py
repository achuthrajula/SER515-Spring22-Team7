laser_joint = """<joint name="laser_joint" type="fixed">
        <child>laser_link</child>
        <parent>chassis</parent>
      </joint>"""


camera_joint = """<joint name="camera_joint" type="fixed">
        <axis>
          <xyz>0 1 0</xyz>
        </axis>
        <pose>1 0 2 0 0 0</pose>
        <parent>chassis</parent>
        <child>camera_link</child>
      </joint>"""


def generate_sensorjoints(sensor_input):
    sensorjoints = []
    if sensor_input == '0':
        sensorjoints.append("")
    elif sensor_input == '1':
        sensorjoints.append(laser_joint)
    elif sensor_input == '2':
        sensorjoints.append(camera_joint)
    elif sensor_input == '3':
        sensorjoints.append(laser_joint)
        sensorjoints.append(camera_joint)

    return sensorjoints