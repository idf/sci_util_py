"""
x_2Dgauss = np.random.multivariate_normal(mu_vec, cov_mat, 10000)
var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
print('actual probability density:', var.pdf([0,0]))
"""
from matplotlib import cm
from matplotlib.delaunay.testfuncs import gauss
from matplotlib.mlab import griddata
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.stats import uniform
from matplotlib.mlab import bivariate_normal
from mpl_toolkits.mplot3d import Axes3D

__author__ = 'Danyang'


def draw_contour():
    x, y, z = 10*np.random.random((3, 10))
    # Set up a regular grid of interpolation points
    xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)

    # Interpolate
    rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
    zi = rbf(xi, yi)

    plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
               extent=[x.min(), x.max(), y.min(), y.max()])
    plt.show()


def plot_countour(x, y, z):
    # define grid.
    xi = np.linspace(-2.1, 2.1, 100)
    yi = np.linspace(-2.1, 2.1, 100)
    # grid the data.
    zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='cubic')
    levels = [0.2, 0.4, 0.6, 0.8, 1.0]
    # contour the gridded data, plotting dots at the randomly spaced data points.
    CS = plt.contour(xi, yi, zi, len(levels), linewidths=0.5, colors='k', levels=levels)
    # CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet)
    CS = plt.contourf(xi, yi, zi, len(levels), cmap=cm.Greys_r, levels=levels)
    plt.colorbar()  # draw colorbar
    # plot data points.
    # plt.scatter(x,y,marker='o',c='b',s=5)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.title('griddata test')
    plt.show()


def draw_2d_gaussian(mean=[0, 0], cov=[[1, 0], [0, 1]]):
    """
    random sampling from gaussian distribution
    :param mean:
    :param cov:
    :return:
    """
    x_2Dgauss = np.random.multivariate_normal(mean, cov, 10000)
    f, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(x_2Dgauss[:, 0], x_2Dgauss[:, 1],
               marker='o', color='green', s=4, alpha=0.3)
    plt.title('10000 samples randomly drawn from a 2D Gaussian distribution')
    plt.ylabel('x2')
    plt.xlabel('x1')
    ftext = 'p(x) ~ N(mu=(0,0)^t, cov=I)'
    plt.figtext(.15, .85, ftext, fontsize=11, ha='left')
    plt.ylim([-4, 4])
    plt.xlim([-4, 4])

    plt.show()


def draw_bivariate_3d(mean=[0, 0], cov=[[1, 0], [0, 1]]):
    """
    http://sebastianraschka.com/Articles/2014_parzen_density_est.html
    :return:
    """
    from matplotlib.mlab import bivariate_normal

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.linspace(-3, 3, 30)
    y = x
    X, Y = np.meshgrid(x, y)

    Z = bivariate_normal(X, Y, mux=mean[0], muy=mean[1], sigmax=cov[0][0], sigmay=cov[1][1], sigmaxy=cov[0][1])

    surf = ax.plot_surface(X, Y, Z, rstride=1,
                           cstride=1, cmap=plt.cm.coolwarm,
                           linewidth=0, antialiased=False
                           )

    ax.set_zlim(0, 0.2)
    ax.zaxis.set_major_locator(plt.LinearLocator(10))
    ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('p(x)')

    plt.title('Bivariate Gaussian distribution')
    fig.colorbar(surf, shrink=0.5, aspect=7, cmap=plt.cm.coolwarm)  # color bar besides

    plt.show()


if __name__=="__main__":
    draw_bivariate_3d()