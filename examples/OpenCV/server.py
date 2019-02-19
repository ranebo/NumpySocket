from numpysocket import NumpySocketServer
import cv2

class NpSocketServer(object):

    def __init__(self, *args, **kwargs):
        self.npSocket = NumpySocketServer()
        self.port = kwargs.get('port', 9999)

    def start(self):
        self.npSocket.start(self.port)
        
    def end(self):
        self.npSocket.end()
        print "Closing"

    def listen(self):
        while(True):
            # Capture frame-by-frame
            frame = self.npSocket.recieveNumpy()
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

if __name__ == '__main__':
    np_server = NpSocketServer()
    try:
        np_server.start()
        np_server.listen()
    except (Exception, KeyboardInterrupt) as e:
        print "Error: ", e
        np_server.end()
