#!/bin/bash

git clone https://github.com/cyberbotics/webots_ros2.git

cd webots_ros2_epuck

echo "launching ros2"

ros2 launch webots_ros2_epuck robot_launch.py

ros2 launch webots_ros2_epuck robot_with_tools_launch.py rviz:=true

echo "successfully installed rviz2"