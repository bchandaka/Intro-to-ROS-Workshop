# Intro-to-ROS-Workshop
This repo includes demo files for my intro to ROS workshop. For ease of use, I will skip the ros install process, so we can get started faster.
Instead of using ros locally, we can use a browser version with everything pre-installed: https://www.theconstructsim.com/

## Demo Package Instructions
1. Setup
    - Create a catkin workspace: `mkdir -p ~/catkin_ws/src`
    - Clone this repo into the `src/` folder of the workspace: `cd ~/catkin_ws/src && git clone https://github.com/bchandaka/Intro-to-ROS-Workshop.git`
    - Download the [sample rosbag](https://drive.google.com/file/d/19iortdU5lFNYnO0v7PV7l99tLThHhzeS/view?usp=sharing) and place it into the `vision_demo/data` folder of this repo 
    - Build the custom package from the workspace folder: `cd ~/catkin_ws && catkin_make`
    - Run the install shell script so ROS2 knows how to run files from your custom package: `source devel/setup.bash`

## Controlling the Turtlebot in theconstructsim
1. `roslaunch turtlebot_gazebo turtlebot_project.launch`
2. `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
3. Move around the turtlebot with your keyboard!
   - try visualizing some of the sensor data with `rviz` too

## Additional Commands
_Tab Completion and `-h` flag are your friends_
- Creating a new catkin package: `catkin_create_pkg <package_name> [depend1] [depend2] [depend3]`
- `rostopic ...`
- `rospack ...`
- `rosbag ...`
- `rviz`
