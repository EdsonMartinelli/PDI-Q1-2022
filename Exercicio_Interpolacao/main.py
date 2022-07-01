import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    img = io.imread('..\\assets\\mario.png')
    nearestNeighborImg = nearest_neighbor(img)
    plt.figure(figsize = (8,8))
    plt.imshow(nearestNeighborImg)
    plt.show()
    io.imwrite('nearest_neighbor.png', nearestNeighborImg)

def nearest_neighbor(img):
    height, width = img.shape[0], img.shape[1]
    result = np.zeros((height * 5, width * 5, 4), dtype = np.uint8)
    for x in range(height):
        for y in range(width):
            result[int(5 * x) : int(5 * x + 5), int(5 * y) : int(5 * y + 5)] = img[x,y]
    return result 

if __name__ == '__main__':
    main()