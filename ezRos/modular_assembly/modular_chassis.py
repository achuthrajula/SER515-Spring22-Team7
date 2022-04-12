
chassis_generator_6x = """<link name='chassis'>
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
              <scale>12 4 4</scale>
              <pose>0 0 7</pose>
            </mesh>
          </geometry>
        </visual>
        <collision name='collision'>
          <geometry>
            <box>
              <size>1.01142 1 0.568726</size>
            </box>
          </geometry>
        </collision>
      </link>"""

chassis_generator_4x = """<link name='chassis'>
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
              <scale>4 4 4</scale>
              <pose>0 0 7</pose>
            </mesh>
          </geometry>
        </visual>
        <collision name='collision'>
          <geometry>
            <box>
              <size>2.01142 1 0.568726</size>
            </box>
          </geometry>
        </collision>
      </link>"""


def generate_chassis(num_wheels):
    if num_wheels == '2' or num_wheels == '4':
        return chassis_generator_4x
    elif num_wheels == '6':
        return chassis_generator_6x
