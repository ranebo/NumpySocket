#!/usr/bin/env python
import freenect
import cv2 as cv
import numpy as np
from numpysocket import NumpySocket

host_ip = 'localhost'  # change me
npSocket = NumpySocket()
npSocket.startServer(host_ip, 9999)

spread = 4
midx = 320
midy = 240
sense_pt1 = (midx - spread, midy - spread)
sense_pt2 = (midx + spread, midy + spread)
sense_rect = (sense_pt1[0], sense_pt1[1], sense_pt2[0] - sense_pt1[0], sense_pt2[1] - sense_pt1[1])

def show_depth():
    global threshold
    global current_depth

    depth, timestamp = freenect.sync_get_depth()
    viewable = depth #frame_convert.full_depth_cv (depth)
    viewable = freenect.sync_get_video()[0]
    npSocket.sendNumpy(viewable)
    #roi = cv.GetSubRect (frame_convert.raw_depth_cv (depth), sense_rect)
    #pix = cv.Avg (roi)[0]
    #(roimin, roimax, a, b) = cv.MinMaxLoc (roi)
    #if roimax < 1090:
    #  dist = 350.0 / (1091 - pix)
    #  print "%f %i %i" % (dist, roimin, roimax)
    #else:
    #  print "XX"

while 1:
    show_depth()
