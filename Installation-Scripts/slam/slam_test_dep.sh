sudo mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws

echo "Downloading turtlebot3 packages from ROBOTIS-GIT"

git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations

echo "Now building dowloaded packages"

cd ~/turtlebot3_ws
colcon build --symlink-install --parallel-workers 1
