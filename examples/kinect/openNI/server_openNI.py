from numpysocket import NumpySocket
import cv2
from scipy.misc import imresize
from time import sleep

host_ip = 'localhost'  # change me
cap = cv2.VideoCapture(0)
opennni = cv2.CAP_OPENNI
npSocket = NumpySocket()
npSocket.startServer(host_ip, 9999)

# Read until video is completed
while(cap.isOpened()):
    #ret, frame = cap.read()
    ret, depth = cap.retrieve(cv2.CAP_OPENNI_DEPTH_MAP)
    ret, frame = cap.retrieve(cv2.CAP_OPENNI_BGR_IMAGE) #cv2.CAP_OPENNI_GRAY_IMAGE
    ref_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_resize = imresize(frame, .5)
    if ret is True:
        npSocket.sendNumpy(frame)
        sleep(1)
    else:
        break
# When everything done, release the video capture object
npSocket.endServer()
cap.release()
