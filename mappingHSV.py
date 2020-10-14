import numpy as np


class MappingHSV(object):
    def __init__(self, img):
        if len(img.shape) == 3:
            h, w, c = img.shape
            img = img.reshape(h * w, c)

        self.h = img[:, 0]
        self.s = img[:, 1]
        self.v = img[:, 2]

    def mapping(self):
        h, s, z = self.hsv_scaling()
        r = np.deg2rad(h)
        x = np.sin(r) * s
        y = np.cos(r) * s
        return np.array([x, y, z]).T

    def hsv_scaling(self):
        H = self.scale_range(self.h, 0, 359)
        S = self.s / 255
        V = self.v / 255
        return (H, S, V)

    def scale_range(self, input, min, max):
        input += -(np.min(input))
        tmp = np.max(input) / (max - min)
        input = input / tmp
        input += min
        return input
