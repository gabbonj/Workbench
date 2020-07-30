import numpy as np
from .transforms import *

class Camera:

    def __init__(self, display, position, forward, near=1.0, far=100.0):
        self.speed = .1
        self.sensitivity = .001
        self.position = position
        self.forward = forward
        self.side = normalize(np.cross(forward, np.array([0, 1, 0])))
        self.up = normalize(np.cross(self.side, forward))
        self.pitch = 0
        self.yaw = 0
        self.proj = self.setFrustum(-(display[0]/display[1])/10, (display[0]/display[1])/10, -1/10, 1/10, near, far)
        self.view = self.get_lookAt(self.forward, self.position)


    def updateCamera(self, forward, position):
        self.position = position
        self.forward = forward
        self.view = self.get_lookAt(self.forward, self.position)


    def setCameraPosition(self, position):
        self.position = position
        self.updateCamera(self.forward, self.position)

    
    def roateCamera(self, pitch, yaw):
        self.pitch = pitch
        self.yaw = yaw
        self.forward[0] = np.cos(yaw) * np.cos(pitch)
        self.forward[1] = np.sin(pitch)
        self.forward[2] = np.sin(yaw) * np.cos(pitch)
        self.forward = normalize(self.forward)
        self.updateCamera(self.forward, self.position)

    def setFrustum(self, l,  r,  b,  t,  n, f):
        mat = np.zeros(16, dtype='float32')
        mat[0]  = 2 * n / (r - l)
        mat[5]  = 2 * n / (t - b)
        mat[8]  = (r + l) / (r - l)
        mat[9]  = (t + b) / (t - b)
        mat[10] = -(f + n) / (f - n)
        mat[11] = -1
        mat[14] = -(2 * f * n) / (f - n)
        mat[15] = 0
        return mat


    def get_lookAt(self, forward, eye):
        fwd = np.array(forward)
        side = normalize(np.cross(fwd, np.array([0, 1, 0])))
        self.side = side
        up = normalize(np.cross(side, fwd))
        self.up = up
        look = np.array([
            [side[0], side[1], side[2], 0],
            [up[0], up[1], up[2], 0],
            [-fwd[0], -fwd[1], -fwd[2], 0],
            [0, 0, 0, 1]
        ], dtype='float32')
        return np.dot(look, get_traslation(-eye[0], -eye[1], -eye[2]))