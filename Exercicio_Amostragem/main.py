import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    PARAMETER = 8
    img = io.imread('..\\assets\\ufabc.png') 
    height, width = np.shape(img)[0], np.shape(img)[1]
    size = (width, height)
    img_crop = img[::PARAMETER, ::PARAMETER]
    plt.figure(figsize = (15,5))
    plt.imshow(img_crop)
    plt.show()
    img_resized = cv.resize(img_crop, size, cv.INTER_NEAREST)
    io.imwrite('result.png', img_resized)


if __name__ == '__main__':
    main()