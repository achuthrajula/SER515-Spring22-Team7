#!/bin/bash

echo "Now testing SLAM installation and generating map to navigate"

echo "Installing dependency packages"

sudo apt update
sudo apt install ros-foxy-turtlebot3-msgs ros-foxy-dynamixel-sdk ros-foxy-hls-lfcd-lds-driver

echo "Creating testing workspace"

bash ./slam_test_dep.sh

echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/src/turtlebot3_gazebo/models' >> ~/.bashrc
source ~/.bashrc

echo 'Spawning multiple terminals to execute the SLAM simulation'

gnome-terminal -- ros2 run turtlebot3_teleop teleop_keyboard

gnome-terminal -- ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True

