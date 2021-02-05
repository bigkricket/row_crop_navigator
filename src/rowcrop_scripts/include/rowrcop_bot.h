#pragma once
#include "ros/ros.h"

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm> 
#include <iterator>  

#include "cv_bridge/cv_bridge.h"
#include "opencv2/highgui/highgui.hpp"
#include <opencv2/core/core.hpp>
#include <opencv2/core/utility.hpp>
#include <opencv2/opencv.hpp>

#include "sensor_msgs/Image.h"
#include <geometry_msgs/Twist.h>
#include <image_transport/image_transport.h>
#include <tf/transform_broadcaster.h>
#include <geometry_msgs/PoseStamped.h>
#include <tf/transform_broadcaster.h>
#include "nav_msgs/Odometry.h"
#include "sensor_msgs/Imu.h"

#include <eigen3/Eigen/Dense>
#include <eigen3/Eigen/QR> 
#include <Eigen/Geometry>

#include <dynamic_reconfigure/server.h>

using namespace cv;
using namespace std;
using namespace Eigen;

namespace rowcrop_vs{
    class RowcropVS {
        /*constructor*/
        RowcropVS();
        /*destructor*/
        ~RowcropVS();
    };
}