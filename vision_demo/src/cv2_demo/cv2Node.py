import rospy
from sensor_msgs.msg import CameraInfo, Image
from cv_bridge import CvBridge
import cv2

class cv2Node:
    def __init__(self, CAMERA_INFO_TOPIC, RGB_TOPIC):
        rospy.init_node('cv2_demo_node', anonymous=True)
        self.camera_info = rospy.wait_for_message(CAMERA_INFO_TOPIC, CameraInfo)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(RGB_TOPIC,Image,self.image_callback)
        self.curImage = None

    def image_callback(self, img_msg: Image):
        self.curImage = self.bridge.imgmsg_to_cv2(img_msg, desired_encoding='passthrough')
        self.curImage = cv2.cvtColor(self.curImage, cv2.COLOR_BGR2RGB)
        cv2.imshow("Orig Image window", self.curImage)
        cv2.waitKey(1)

    def run(self):
        rospy.spin()