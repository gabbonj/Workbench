import numpy as np

def normalize(v):
    m = np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    if m == 0:
        m = .00001
    return v / m


def get_rot(angle, axis_ix):
    s = np.sin(angle)
    c = np.cos(angle)
    if axis_ix == 0:
        return np.array([[ 1,  0,  0, 0],
                        [ 0,  c, -s, 0],
                        [ 0,  s,  c, 0],
                        [ 0,  0,  0, 1]], dtype='float32')
    elif axis_ix == 1:
        return np.array([[ c,  0,  s, 0],
                        [ 0,  1,  0, 0],
                        [-s,  0,  c, 0],
                        [ 0,  0,  0, 1]], dtype='float32')
    elif axis_ix == 2:
        return np.array([[ c, -s,  0, 0],
                        [ s,  c,  0, 0],
                        [ 0,  0,  1, 0],
                        [ 0,  0,  0, 1]], dtype='float32')


def get_traslation(x, y, z):
    out = np.array([[ 1,  0,  0, x],
                    [ 0,  1,  0, y],
                    [ 0,  0,  1, z],
                    [ 0,  0,  0, 1]], dtype='float32')
    return out
