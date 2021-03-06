#!/usr/bin/env python3

"""
ON THE RASPI: roslaunch raspicam_node camerav2_320x240.launch enable_raw:=true
   0------------------> x (cols) Image Frame
   |
   |        c    Camera frame
   |         o---> x
   |         |
   |         V y
   |
   V y (rows)
SUBSCRIBES TO:
    /raspicam_node/image: Source image topic
    
PUBLISHES TO:
    /crop/image_crop : image with detected crop and search window
    /crop/image_mask : masking    
    /crop/point_crop : crop position in adimensional values wrt. camera frame
"""


#--- Allow relative importing
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    
import sys
import rospy
import cv2
import time

from std_msgs.msg           import String
from sensor_msgs.msg        import Image
from geometry_msgs.msg      import Point
from cv_bridge              import CvBridge, CvBridgeError
from include.crop_detector  import *


class cropDetector:

    def __init__(self, thr_min, thr_max, blur=15, crop_params=None, detection_window=None):
    
        self.set_threshold(thr_min, thr_max)
        self.set_blur(blur)
        self.set_crop_params(crop_params)
        self.detection_window = detection_window
        
        self._t0 = time.time()
        
        self.crop_point = Point()
    
        print (">> Publishing image to topic image_crop")
        self.image_pub = rospy.Publisher("/crop/image_crop",Image,queue_size=1)
        self.mask_pub = rospy.Publisher("/crop/image_mask",Image,queue_size=1)
        print (">> Publishing position to topic point_crop")
        self.crop_pub  = rospy.Publisher("/crop/point_crop",Point,queue_size=1)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/agbot/camera1/image_raw",Image,self.callback)
        print ("<< Subscribed to topic /agbot/image")
        
    def set_threshold(self, thr_min, thr_max):
        self._threshold = [thr_min, thr_max]
        
    def set_blur(self, blur):
        self._blur = blur
      
    def set_crop_params(self, crop_params):
        self._crop_params = crop_params
        
    # def get_crop_relative_position(self, cv_image, keyPoint):
        # rows = float(cv_image.shape[0])
        # cols = float(cv_image.shape[1])
        # # print(rows, cols)
        # center_x    = 0.5*cols
        # center_y    = 0.5*rows
        # # print(center_x)
        # x = (keyPoint.pt[0] - center_x)/(center_x)
        # y = (keyPoint.pt[1] - center_y)/(center_y)
        # return(x,y)
        
        
    def callback(self,data):
        #--- Assuming image is 320x240
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows,cols,channels) = cv_image.shape
        if cols > 60 and rows > 60 :
            #--- Detect crops
            keypoints, mask   = crop_detect(cv_image, self._threshold[0], self._threshold[1], self._blur,
                                            crop_params=self._crop_params, search_window=self.detection_window )
            #--- Draw search window and crops
            cv_image    = blur_outside(cv_image, 10, self.detection_window)

            cv_image    = draw_window(cv_image, self.detection_window, line=1)
            cv_image    = draw_frame(cv_image)
            
            cv_image    = draw_keypoints(cv_image, keypoints) 
            
            cv2.imshow("Image window", cv_image)
            cv2.waitKey(3)

            try:
                self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
                self.mask_pub.publish(self.bridge.cv2_to_imgmsg(mask, "8UC1"))
            except CvBridgeError as e:
                print(e)            

            for i, keyPoint in enumerate(keypoints):
                #--- Here you can implement some tracking algorithm to filter multiple detections
                #--- We are simply getting the first result
                x = keyPoint.pt[0]
                y = keyPoint.pt[1]
                s = keyPoint.size
                print ("kp %d: s = %3d   x = %3d  y= %3d"%(i, s, x, y))
                
                #--- Find x and y position in camera adimensional frame
                x, y = get_crop_relative_position(cv_image, keyPoint)
                
                self.crop_point.x = x
                self.crop_point.y = y
                self.crop_pub.publish(self.crop_point) 
                break
                    
            fps = 1.0/(time.time()-self._t0)
            self._t0 = time.time()
            
def main(args):
    green_min = (77,40,0)
    green_max = (101, 255, 255) 
    # green_min = (82,31,62)
    # green_max = (106, 116, 193)     
    green_min = (25,17,47)
    green_max = (126, 255, 255)     
    
    blur     = 5
    min_size = 10
    max_size = 40
    
    #--- detection window respect to camera frame in [x_min, y_min, x_max, y_max] adimensional (0 to 1)
    x_min   = 0.1
    x_max   = 0.9
    y_min   = 0.4
    y_max   = 0.9
    
    detection_window = [x_min, y_min, x_max, y_max]
    
    params = cv2.SimpleBlobDetector_Params()
         
    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 100
     
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 20
    params.maxArea = 20000
     
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
     
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.2
     
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.7   

    ic = cropDetector(green_min, green_max, blur, params, detection_window)
    rospy.init_node('crop_detector', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)