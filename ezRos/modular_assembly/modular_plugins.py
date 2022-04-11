plugin_boiler_plate = """<ros>
                    <namespace>/demo</namespace>
                    <remapping>cmd_vel:=cmd_demo</remapping>
                    <remapping>odom:=odom_demo</remapping>
                </ros>


                <!-- limits -->
                <max_wheel_torque>20</max_wheel_torque>
                <max_wheel_acceleration>1.0</max_wheel_acceleration>

                <!-- output -->
                <publish_odom>true</publish_odom>
                <publish_odom_tf>true</publish_odom_tf>
                <publish_wheel_tf>true</publish_wheel_tf>

                <odometry_frame>odom_demo</odometry_frame>
                <robot_base_frame>chassis</robot_base_frame>

            </plugin>"""


plugin_generator_2x = """ <plugin name='diff_drive' filename='libgazebo_ros_diff_drive.so'>

                <!-- wheels -->
                <left_joint>left_wheel_joint</left_joint>
                <right_joint>right_wheel_joint</right_joint>

                <!-- wheel radius -->
                <wheel_separation>1.25</wheel_separation>
                <wheel_diameter>0.6</wheel_diameter>"""

plugin_generator_4x = """<plugin name='skid_steer_drive' filename='libgazebo_ros_diff_drive.so'>

          <!-- Number of wheel pairs -->
          <num_wheel_pairs>2</num_wheel_pairs>
          
          <!-- wheels0 -->
          <left_joint>left_wheel_joint_0</left_joint>
          <right_joint>right_wheel_joint_0</right_joint>

          <!-- wheels1-->
          <left_joint>left_wheel_joint_1</left_joint>
          <right_joint>right_wheel_joint_1</right_joint>

          <!-- kinematics -->
          <wheel_separation>1.25</wheel_separation>
          <wheel_separation>1.25</wheel_separation>

          <wheel_diameter>1.0</wheel_diameter>
          <wheel_diameter>0.6</wheel_diameter>"""

plugin_generator_6x = """<plugin name='diff_drive' filename='libgazebo_ros_diff_drive.so'>
              
        <!-- wheels -->
        <left_joint>left_wheel_joint_0</left_joint>
        <right_joint>right_wheel_joint_0</right_joint>
        <mid_left_joint>left_wheel_joint_1</mid_left_joint>
        <mid_right_joint>right_wheel_joint_1</mid_right_joint>
        <back_left_joint>left_wheel_joint_2</back_left_joint>
        <back_right_joint>right_wheel_joint_2</back_right_joint>

        <!-- kinematics -->
        <wheel_separation>1.25</wheel_separation>
        <wheel_diameter>0.6</wheel_diameter>"""


def generate_plugins(num_wheels):
    if num_wheels == '6':
        return plugin_generator_6x + plugin_boiler_plate
    elif num_wheels == '4':
        return plugin_generator_4x + plugin_boiler_plate
    elif num_wheels == '2':
        return plugin_generator_2x + plugin_boiler_plate
