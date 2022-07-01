import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    img = io.imread('..\\assets\\ufabc.png') 
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    D1 = np.array([[  0, 128],
                   [192,  62]])

    D2 = np.array([[  0, 128,  32, 160],
                   [192,  62, 224,  96],
                   [ 48, 176,  16, 144],
                   [240, 112, 208,  80]])

    img = dithering(img, D2)

    plt.figure(figsize = (15,5))
    plt.imshow(img, cmap='gray')
    plt.show()
    io.imwrite('result.png', img)

def dithering(img, D):
    height, width = img.shape[0], img.shape[1]
    result = np.zeros((height, width), dtype = np.uint8)
    height_D, width_D = D.shape[0], D.shape[1]
    times_height, times_width = int(np.ceil(height / height_D)), int(np.ceil(width / width_D))
    matrix = np.tile(D, (times_height,times_width))

    for x in range(height):
        for y in range(width):
            if img[x, y] > matrix[x, y] :
                result[x, y] = 255
            else:
                result[x, y] = 0
    return result

if __name__ == '__main__':
    main()