from numpysocket import NumpySocketClient
import cv2
from scipy.misc import imresize

# host_ip = 'localhost'  # change me
# cap = cv2.VideoCapture(0)
# npSocket = NumpySocket()
# npSocket.startServer(host_ip, 9999)

# # Read until video is completed
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     ref_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame_resize = imresize(ref_frame, .5)
#     if ret is True:
#         npSocket.sendNumpy(frame_resize)
#     else:
#         break
# # When everything done, release the video capture object
# npSocket.endServer()
# cap.release()


class NpSocketClient(object):

    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', 'localhost')  # change me
        self.port = kwargs.get('port', 9999)
        self.cap = cv2.VideoCapture(0)
        self.npSocket = NumpySocketClient()

    def start(self):
        self.npSocket.start(self.host, self.port)

    def end(self):
        self.npSocket.end()
        self.cap.release()

    def cap_cam(self):
            # Read until video is completed
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            # ref_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_resize = imresize(frame, .5)
            if ret is True:
                self.npSocket.sendNumpy(frame_resize)
            else:
                break

if __name__ == '__main__':
    np_client = NpSocketClient()
    try:
        np_client.start()
        np_client.cap_cam()
    except (Exception, KeyboardInterrupt) as e:
        print "Error: ", e
        np_client.end()
