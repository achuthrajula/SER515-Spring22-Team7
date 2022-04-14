chassis_generator = {
  '2x_4x': {
    'scale': '4 4 4',
    'size': '2.01142 1 0.568726',
  },
  '6x': {
    'scale': '12 4 4',
    'size': '1.01142 1 0.568726',
  },
  '8x': {
    'scale': '11 4 4',
    'size': '1.01142 1 0.568726',
  },
}

def generate_chassis(num_wheels):
    if num_wheels == '2' or num_wheels == '4':
        value = chassis_generator['2x_4x']
    elif num_wheels == '6':
        value = chassis_generator['6x']
    elif num_wheels == '8':
        value = chassis_generator['8x']

    chassis = f"""<link name='chassis'>
        <pose>-0.2 -0 0.2 0 -0 0</pose>
        <inertial>
          <mass>1.14395</mass>
          <inertia>
            <ixx>0.126164</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.416519</iyy>
            <iyz>0</iyz>
            <izz>0.481014</izz>
          </inertia>
        </inertial>
        <visual name='visual'>
          <geometry>
            <mesh>
              <uri>model://pioneer3at/meshes/chassis.dae</uri>
              <scale>{value['scale']}</scale>
              <pose>0 0 7</pose>
            </mesh>
          </geometry>
        </visual>
        <collision name='collision'>
          <geometry>
            <box>
              <size>{value['size']}</size>
            </box>
          </geometry>
        </collision>
      </link>"""
    return chassis