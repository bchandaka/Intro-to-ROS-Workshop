#!/usr/bin/env python3
from cv2_demo.cv2Node import cv2Node
import numpy as np

RGB_TOPIC = "/rgb"
CAMERA_INFO_TOPIC = "/camera_info"

def main():
    cv2_node = cv2Node(
        CAMERA_INFO_TOPIC,
        RGB_TOPIC
    )
    cv2_node.run()

if __name__ == '__main__':
    main()