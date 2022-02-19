## SER515

### Instructions to move rover around

Assuming that `ros2`, `gazebo` and `python` are already installed on the workspace, the script will be executed using the following command:

Step 1: In the terminal use `python3 move_rover.py` and give `'1'` as input to start gazebo with the rover.

Step 2: In the terminal use `python3 move_rover.py` and give 2-6 commands to engage movement in the rover.

Note: You may find the required documentation for installation of the above mentioned packages here:

- [Ros2](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Binary.html)
- [Gazebo](http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros)
- [Python](https://www.python.org/downloads/release/python-3810/)

There is a `/Rover Environment` directory in the workspace. Make sure to insert `testing-ground` on `gazebo` before running the script. This ensures that the rover never goes out of the virtual environment, as this may lead to unexpected behaviour.
