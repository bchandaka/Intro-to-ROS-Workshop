#!bin/sh
rosbag play "$(rospack find vision_demo)"/data/sim_gem_moving.bag \
    /gem/velodyne_points:=/cloud \
    /gem/front_single_camera/camera_info:=/camera_info \
    /gem/front_single_camera/image_raw:=/rgb