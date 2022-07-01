import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    PARAMETER = 1
    img = io.imread('..\\assets\\ufabc.png') 
    quantizationImg = quantization(img, PARAMETER)
    plt.figure(figsize = (15,5))
    plt.imshow(quantizationImg)
    plt.show()
    io.imwrite('result.png', quantizationImg)


def scale_det(value, divisions):
    distInterval = 255 / divisions
    valuePart = round(value / distInterval)
    return int( (distInterval * valuePart))

def quantization(img, divisions):
    height, width, color = np.shape(img)
    print(np.shape(img))
    result = np.zeros((height, width, color), dtype=np.uint8)
    for x in range(height):
        for y in range(width):
            for z in range(color):
                result[x][y][z] = scale_det(img[x][y][z], divisions)
    return result

if __name__ == '__main__':
    main()