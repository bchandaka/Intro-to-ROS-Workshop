# Intro-to-ROS-Workshop
This repo includes demo files for my intro to ROS workshop. For ease of use, I will skip the ros install process, so we can get started faster.
Instead of using ros locally, we can use a browser version with everything pre-installed: https://www.theconstructsim.com/

## Instructions
1. Setup
    - Create a colcon workspace: `mkdir -p ~/demo_ws/src`
    - Clone this repo into the `src/` folder of the workspace: `cd ~/demo_ws/src && git clone https://github.com/bchandaka/Intro-to-ROS-Workshop.git`
    - Build the custom package from the workspace folder: `cd ~/demo_ws && colcon build`
    - Run the install shell script so ROS2 knows how to run files from your custom package: `source install/setup.bash`
