import numpy as np

__author__ = 'Danyang'


def parzen_estimation(x_samples, point_x, h):
    """
    Implementation of a hypercube kernel for Parzen-window estimation.

    :param x_samples: training sample, matrix of row vector
    :param point_x: point x for density estimation, col vector
    :param h: window width
    :return: returns the predicted pdf as float.
    """
    k_n = 0
    for row in x_samples:
        x_i = (point_x - row[:, np.newaxis]) / h
        for row in x_i:
            if np.abs(row) > 1/2:
                break
        else:  # "completion-else"
            k_n += 1

    return (k_n / len(x_samples)) / (h**point_x.shape[1])