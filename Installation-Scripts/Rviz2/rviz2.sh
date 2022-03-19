#!/bin/bash

sudo mkdir -p ~/rviz2_ws/src

cd ~/rviz2_ws/src

echo "cloning packages for rviz"

git clone https://github.com/ros2/rviz.git

echo "building the cloned packages"

colcon build --merge-install