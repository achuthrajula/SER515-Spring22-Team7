echo "Starting ROS2 Installation Tests"

echo "Installing turtlesim if not installed previously"

sudo apt update
sudo apt install ros-foxy-turtlesim

echo "Trying to run turtlesim using ros2"

source /opt/ros/foxy/setup.bash

ros2 run turtlesim turtlesim_node

echo "Ros2 Installation Tests Finished Successfully"
