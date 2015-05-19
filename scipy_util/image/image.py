import cv2
import numpy as np
__author__ = 'Daniel'


def imshow(mat, img_name="Image Name"):
    """
    Display the image and wait
    :param mat: normally the data type is 8-bit int, for other cases:
    http://docs.opencv.org/modules/highgui/doc/user_interface.html?highlight=imshow#cv2.imshow
    :param img_name:
    :return:
    """
    cv2.imshow(img_name, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def random_img(size=(400, 400)):
    """
    Gray scale image with random noise 
    """
    mat = np.random.randint(0, 255, size)
    mat = np.asarray(mat, dtype=np.int8)
    return mat


def blurred_img(size=(400, 400)):
    """
    Gaussian blur
    """
    mat = random_img(size)
    kernel = cv2.getGaussianKernel(129, 7)
    mat = cv2.filter2D(mat, cv2.CV_8UC3, kernel)  # convolve
    mat = np.asarray(mat, dtype=np.int8)
    return mat


if __name__ == "__main__":
    imshow(random_img())
    imshow(blurred_img())