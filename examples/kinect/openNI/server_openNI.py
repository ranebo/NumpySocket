from numpysocket import NumpySocket
import cv2
from scipy.misc import imresize
from time import sleep

host_ip = 'localhost'  # change me
cap = cv2.VideoCapture(0)
opennni = cv2.CAP_OPENNI
npSocket = NumpySocket()
npSocket.startServer(host_ip, 9999)

# OPENNI Types
#CAP_OPENNI_DEPTH_MAP - depth values in mm (CV_16UC1)
#CAP_OPENNI_POINT_CLOUD_MAP - XYZ in meters (CV_32FC3)
#CAP_OPENNI_DISPARITY_MAP - disparity in pixels (CV_8UC1)
#CAP_OPENNI_DISPARITY_MAP_32F - disparity in pixels (CV_32FC1)
#CAP_OPENNI_VALID_DEPTH_MASK - mask of valid pixels (not ocluded, not shaded etc.) (CV_8UC1)
#CAP_OPENNI_BGR_IMAGE - color image (CV_8UC3)
#CAP_OPENNI_GRAY_IMAGE - gray image (CV_8UC1)

CV_TYPE = [
	cv2.CAP_OPENNI_DEPTH_MAP, 
	cv2.CAP_OPENNI_POINT_CLOUD_MAP, 
	cv2.CAP_OPENNI_DISPARITY_MAP, 
	cv2.CAP_OPENNI_DISPARITY_MAP_32F, 
	cv2.CAP_OPENNI_VALID_DEPTH_MASK, 
	cv2.CAP_OPENNI_BGR_IMAGE, 
	cv2.CAP_OPENNI_GRAY_IMAGE]

# Read until video is completed
while(cap.isOpened()):
    #ret, depth = cap.read()
    if(cap.grab()):
        ret, depth = cap.retrieve(0, CV_TYPE[0])
    else:
        break    
    
    if ret is True:
        npSocket.sendNumpy(imresize(depth,.5))
        sleep(1)
    else:
        break
# When everything done, release the video capture object
npSocket.endServer()
cap.release()
