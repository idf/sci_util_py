__author__ = 'Danyang'

import numpy as np
import numpy.linalg as la


def transpose(A):
    """
    For transposing 1D array, it's working exactly as it's supposed to. The transpose of a 1D array is still a 1D array!
    (If you're used to matlab, it fundamentally doesn't have a concept of a 1D array. Matlab's "1D" arrays are 2D.)
    :param A:
    :return:
    """
    A.transpose()
    return A.T


def inverse(A):
    return la.inv(A)

def to2D(A):
    """
    from array([1, 2, 3]) to array([[1, 2, 3]])
    :param A:
    :return:
    """
    return A[np.newaxis]