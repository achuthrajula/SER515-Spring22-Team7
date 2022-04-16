laser = """
              <collision name="collision-top">
                <pose>0 0 0.0205 0 0 0</pose>
                <geometry>
                  <cylinder>
                    <radius>0.021</radius>
                    <length>0.029</length>
                  </cylinder>
                </geometry>
              </collision>
              
        <sensor name="laser" type="ray">
          <pose>0.01 0 0.0175 0 -0 0</pose>
                <ray>
                  <scan>
                    <horizontal>
                      <samples>181</samples>
                      <resolution>1</resolution>
                      <min_angle>-1.57080</min_angle>
                      <max_angle>1.57080</max_angle>
                    </horizontal>
                  </scan>
                  <range>
                    <min>0.08</min>
                    <max>10</max>
                    <resolution>0.05</resolution>
                  </range>
                </ray>
                <always_on>1</always_on>
                <update_rate>10</update_rate>
                <visualize>true</visualize>
      
                <plugin name='laser' filename='libgazebo_ros_ray_sensor.so'>
                  <ros>
                    <namespace>/demo</namespace>
                    <argument>--ros-args --remap ~/out:=scan</argument>
                  </ros>
                  <output_type>sensor_msgs/LaserScan</output_type>
                </plugin>
        </sensor>
            </link>"""

camera = """
    <sensor type="camera" name="camera1">
      <update_rate>30.0</update_rate>
      <camera name="head">
        <horizontal_fov>1.3962634</horizontal_fov>
        <image>
          <width>800</width>
          <height>800</height>
          <format>R8G8B8</format>
        </image>
        <clip>
          <near>0.02</near>
          <far>300</far>
        </clip>
        <noise>
          <type>gaussian</type>
          <mean>0.0</mean>
          <stddev>0.007</stddev>
        </noise>
      </camera>
      <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
        <alwaysOn>true</alwaysOn>
        <updateRate>0.0</updateRate>
        <cameraName>rrbot/camera1</cameraName>
        <imageTopicName>image_raw</imageTopicName>
        <cameraInfoTopicName>camera_info</cameraInfoTopicName>
        <frameName>camera_link</frameName>
        <hackBaseline>0.07</hackBaseline>
        <distortionK1>0.0</distortionK1>
        <distortionK2>0.0</distortionK2>
        <distortionK3>0.0</distortionK3>
        <distortionT1>0.0</distortionT1>
        <distortionT2>0.0</distortionT2>
      </plugin>

    </sensor>
  </link>"""

sensor_generator = {
  'laser': {
    'id': laser,
    'name':'laser_link',
    'pose_front': '0.7 0 0.62 0 0 0',
    'pose_back': '-1 0 0.62 0 0 3.15',
    'collision_pose' : '0 0 -0.0145 0 0 0',
    'collision_size' : '0.05 0.05 0.041',
    'visual_geometry': """
            <mesh>
              <uri>model://hokuyo/meshes/hokuyo.dae</uri>
            </mesh>
    """,
    'mass': '0.1',
    },
  'camera': {
    'id':camera,
    'name': 'camera_link',
    'pose_front': '0.6 0.2 0.68 0 0 0',
    'pose_back': '-0.8 0.2 0.68 0 0 3.15',
    'collision_pose' : '0 0 0 0 0 0',
    'collision_size' : '0.15 0.3 0.15',
    'visual_geometry': """
            <box>
              <size>0.15 0.15 0.15</size>
            </box>
    """,
    'mass': '1e-5',
    },
}


def generate_sensors(req_sensors):
    iterator = []
    sensorsList = []
    if not req_sensors:
        sensorsList.append("")
    elif 'laser' in req_sensors and 'camera' not in req_sensors:
        iterator.append('laser')
    elif 'laser' not in req_sensors and 'camera' in req_sensors:
        iterator.append('camera')
    elif 'laser' in req_sensors and 'camera' in req_sensors:
        iterator.extend(['laser','camera'])

    for value in iterator:
      data = sensor_generator[value]
      sensor_position_input =  input(f"""
            Where would you like to place {value} sensor:\n
            [1] Front
            [2] Back
            """)
      sensor_position_data = ""
      if sensor_position_input == '1':
        sensor_position_data = data['pose_front']
      elif sensor_position_input == '2':
        sensor_position_data = data['pose_back']
      else:
        sensor_position_data = data['pose_front']
      joint = f"""
      <link name='{data['name']}'>
    <collision name="collision-base">
          <pose>{data['collision_pose']}</pose>
          <geometry>
            <box>
              <size>{data['collision_size']}</size>
            </box>
          </geometry>
        </collision>
        <pose>{sensor_position_data}</pose>
        <visual name="visual">
          <pose>0 0 0 0 0 0</pose>
          <geometry>
            {data['visual_geometry']}
          </geometry>
        </visual>
        <inertial>
          <mass>{data['mass']}</mass>
        </inertial>
      """
      sensorsList.append(joint+data['id'])
    return sensorsList