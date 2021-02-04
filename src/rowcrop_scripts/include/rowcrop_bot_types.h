#pragma once
#include <vector>
#include <eigen3/Eigen/Dense>
#include <opencv2/core/core.hpp>

using namespace cv;
using namespace std;
using namespace Eigen;

namespace agribot_vs {
    
/**
 * @brief object of camera containing features and 
 * neighbourhood properties 
 */
struct camera{
  Mat image;
  vector<int> id;
  vector<int> nh_id;
  vector<Point2f> points;
  vector<Point2f> nh_points; 
  vector<vector<Point>> contours;
  vector<Vec4i> lines;
  // set camera Intrinsics
  int height;
  int width;
  int f_mm;                // focal length (in mm)
  int s_w;                 // sensor width (in mm)
  vector<Point2f> nh_ex;
  Neighbourhood nh;
} ;

}