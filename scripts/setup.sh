#!/bin/bash
# Project Aegis: USV Setup Script

echo "--- Initializing USV Environment ---"

# Install ROS2 Humble dependencies
sudo apt update
sudo apt install -y ros-humble-desktop-full
sudo apt install -y python3-colcon-common-extensions python3-rosdep python3-argcomplete

# Source ROS2
source /opt/ros/humble/setup.bash

# Initialize rosdep
if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
    sudo rosdep init
fi
rosdep update

echo "--- Setup Complete ---"
