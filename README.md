# SER515: Autonomous Rover Development Environment

This repository is a python module to make ROS2 easier to implement using a Object Oriented paradigm.

<br>

### Local setup

<br>

After cloning this repo and navigating to the root directory, you can install it using the following command:

```
python3 -m setup.py develop
```

### Run

```
ezRos
```

<br />

### What we currently Offer

<br />

- Launch a testing ground for the testing the developed rover, also modularly assembles the rover and mounts the sensors as required by the user.

- Controller to manually override the rover movement which is a replica of ROS2's teleop keyboard.

- Environment setup lets user install all the required packages and libraries for development workspace in a hassle free manner.

- Test Installations lets the user run test scripts to verify the integrity of the packages and libraries installed.

- Launch ROS2, fires ROS2 with the user specified nodes and sets up the network. As a placeholder we currently put a couple of turtlesim nodes

- Rover autonomously navigate through the maze without collisions and without human intervention.

- Random obstacles generation, offers to generate obstacles by taking details of length spread area (assuming to be a square), number of obstacles and minimum distance between them.

- Random maze generation, offers to generate a maze by taking details of length spread area (assuming to be a square), number of walls, minimum distance between them and length of each wall with definite boundaries.

### Credits

- [Addison Sears-Collins](https://automaticaddison.com)
- [ROS2](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Binary.html)
- [Gazebo](http://gazebosim.org/tutorials?tut=install_ubuntu)
- [teleop](https://index.ros.org/p/teleop_twist_keyboard/github-ros2-teleop_twist_keyboard/#foxy)

### Contributors

- Prasuna Bumadi
- Nikitha Reddy Junuthula
- Achuth Reddy Rajula
- Varshik Sonti
- Rajiv Kashyap Jalakam
- Shivani Patel
