#!/usr/bin/env python

import socket
import numpy as np
from cStringIO import StringIO


class NumpySocketServer():
    def __init__(self):
        self.address = ''
        self.port = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, port):
        self.port = port

        self.socket.bind((self.address, self.port)) # if external: self.address = socket.gethostname()
        self.socket.listen(1)
        print 'waiting for a connection...'
        self.client_connection, self.client_address = self.socket.accept()
        print 'connected to ', self.client_address[0]

    def end(self):
        self.client_connection.shutdown(1)
        self.client_connection.close()
        self.socket.shutdown(1)
        self.socket.close()

    def recieveNumpy(self):
        length = None
        ultimate_buffer = ""
        while True:
            data = self.client_connection.recv(1024)
            ultimate_buffer += data
            if len(ultimate_buffer) == length:
                break
            while True:
                if length is None:
                    if ':' not in ultimate_buffer:
                        break
                    # remove the length bytes from the front of ultimate_buffer
                    # leave any remaining bytes in the ultimate_buffer!
                    length_str, ignored, ultimate_buffer = ultimate_buffer.partition(':')
                    length = int(length_str)
                if len(ultimate_buffer) < length:
                    break
                # split off the full message from the remaining bytes
                # leave any remaining bytes in the ultimate_buffer!
                ultimate_buffer = ultimate_buffer[length:]
                length = None
                break
        final_image = np.load(StringIO(ultimate_buffer))['frame']
        print 'frame received'
        return final_image

class NumpySocketClient():
    def __init__(self):
        self.address = 0
        self.port = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, address, port):
        self.address = address
        self.port = port
        try:
            self.socket.connect((self.address, self.port))
            print 'Connected to %s on port %s' % (self.address, self.port)
        except socket.error, e:
            print 'Connection to %s on port %s failed: %s' % (self.address, self.port, e)
            return

    def end(self):
        self.socket.shutdown(1)
        self.socket.close()

    def sendNumpy(self, image):
        if not isinstance(image, np.ndarray):
            print 'not a valid numpy image'
            return
        f = StringIO()
        np.savez_compressed(f, frame=image)
        f.seek(0)
        out = f.read()
        val = "{0}:".format(len(f.getvalue()))  # prepend length of array
        out = val + out
        try:
            self.socket.sendall(out)
            print 'image sent'
        except Exception:
            exit()
