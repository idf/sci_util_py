"""
x_2Dgauss = np.random.multivariate_normal(mu_vec, cov_mat, 10000)
var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
print('actual probability density:', var.pdf([0,0]))
"""
import numpy as np
from scipy.stats import multivariate_normal

__author__ = 'Danyang'
