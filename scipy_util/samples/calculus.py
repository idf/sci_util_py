import numpy as np
from scipy import integrate

__author__ = 'Danyang'


def integral(f, l, u):
    """
    >>> integrate.quad(lambda x: x**3, 0, 1)

    np.Inf available

    for double integral:
    http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
    """
    ret = integrate.quad(f, l, u)
    return ret