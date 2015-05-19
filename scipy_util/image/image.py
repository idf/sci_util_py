import cv2
import numpy as np
__author__ = 'Daniel'


def mat2img(mat, img_name="Image Name"):
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

if __name__=="__main__":
    mat = np.random.randint(0, 255, (400, 400))
    mat = np.asarray(mat, dtype=np.int8)
    mat2img(mat)