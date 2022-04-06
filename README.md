# Intro-to-ROS-Workshop
This repo includes demo files for my intro to ROS workshop. For ease of use, I will skip the ros install process, so we can get started faster.
Instead of using ros locally, we can use a browser version with everything pre-installed: https://www.theconstructsim.com/

## ROS1 Instructions
1. Setup
    - Create a catkin workspace: `mkdir -p ~/catkin_ws/src`
    - Clone this repo into the `src/` folder of the workspace: `cd ~/catkin_ws/src && git clone https://github.com/bchandaka/Intro-to-ROS-Workshop.git`
    - Build the custom package from the workspace folder: `cd ~/catkin_ws && catkin_make`
    - Run the install shell script so ROS2 knows how to run files from your custom package: `source devel/setup.bash`


## Additional Commands
_Tab Completion is your friend_
- Creating a new catkin package: `catkin_create_pkg <package_name> [depend1] [depend2] [depend3]`
- 