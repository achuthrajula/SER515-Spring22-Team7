echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.zshrc
echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/src/turtlebot3_gazebo/models' >> ~/.bashrc
echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/src/turtlebot3_gazebo/models' >> ~/.zshrc
source ~/.bashrc
source ~/.zshrc

source /opt/ros/foxy/setup.bash
source /opt/ros/foxy/setup.zsh

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py > /dev/null &
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/map.yaml