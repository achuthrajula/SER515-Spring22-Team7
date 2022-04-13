laser = """<link name="laser_link">
              <inertial>
                <!-- Mass of the laser range finder in kg -->
                <mass>0.1</mass>
              </inertial>
              <!-- Position is towards the front of the robot -->
              <!-- Laser finder is mounted on top -->
              <pose>0.7 0 0.62 0 0 0</pose>
              
              <!-- Add a mesh to make it more visually appealing -->
              <visual name="visual">
                <geometry>
                  <mesh>
                    <uri>model://hokuyo/meshes/hokuyo.dae</uri>
                  </mesh>
                </geometry>
              </visual>
              
              <!-- Collision properties of the base of the laser range finder-->
              <collision name="collision-base">
                <pose>0 0 -0.0145 0 0 0</pose>
                <geometry>
                  <box>
                    <size>0.05 0.05 0.041</size>
                  </box>
                </geometry>
              </collision>
              <!-- Collision properties of the top of the laser range finder-->
              <collision name="collision-top">
                <pose>0 0 0.0205 0 0 0</pose>
                <geometry>
                  <cylinder>
                    <radius>0.021</radius>
                    <length>0.029</length>
                  </cylinder>
                </geometry>
              </collision>
              
              <!-- Describes the type and properties of the sensor -->
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

camera = """<link name="camera_link">
  <collision name="collision-base">
          <pose>0 0 0 0 0 0</pose>
          <geometry>
            <box>
              <size>0.15 0.15 0.15</size>
            </box>
          </geometry>
        </collision>
        <pose>0.7 0.3 0.68 0 0 0</pose>

        <visual name="visual-base">
          <pose>0 0 0 0 0 0</pose>
          <geometry>
            <box>
              <size>0.15 0.15 0.15</size>
            </box>
          </geometry>
          <material>
            <name>red</name>
          </material>
        </visual>

        <inertial>
          <mass>1e-5</mass>
          <pose>0 0 0 0 0 0</pose>
          <inertia>
            <ixx>1e-6</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>1e-6</iyy>
            <iyz>0</iyz>
            <izz>1e-6</izz>
          </inertia>
        </inertial>
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
          <!-- Noise is sampled independently per pixel on each frame.
               That pixel's noise value is added to each of its color
               channels, which at that point lie in the range [0,1]. -->
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


def generate_sensors():
    sensor_input = input("""
        Enter the sensors for the rover\n
        [0] No Sensors
        [1] Laser
        [2] Camera
        [3] Laser and Camera
        """)
    sensorsList = []
    if sensor_input == '0':
        sensorsList.append("")
    elif sensor_input == '1':
        sensorsList.append(laser)
    elif sensor_input == '2':
        sensorsList.append(camera)
    elif sensor_input == '3':
        sensorsList.append(laser)
        sensorsList.append(camera)
    return sensorsList, sensor_input