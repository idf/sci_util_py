import numpy as np
import numpy.linalg as la


__author__ = 'Danyang'


def transpose(A):
    """
    For transposing 1D array, it's working exactly as it's supposed to. The transpose of a 1D array is still a 1D array!
    (If you're used to matlab, it fundamentally doesn't have a concept of a 1D array. Matlab's "1D" arrays are 2D.)
    """
    A.transpose()
    return A.T


def inverse(A):
    return la.inv(A)


def to2D(A):
    """
    From array([1, 2, 3]) to array([[1, 2, 3]])
    """
    return A[np.newaxis]


def to1D(A):
    """
    Matrix unrolling
    No side effect
    Different from A.reshape(1, -1)
    """
    return A.ravel()


def unroll(A):
    """
    No side effect
    """
    return A.reshape(1, -1)

