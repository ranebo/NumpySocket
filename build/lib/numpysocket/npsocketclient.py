#!/usr/bin/env python

import socket
import numpy as np
from cStringIO import StringIO


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
