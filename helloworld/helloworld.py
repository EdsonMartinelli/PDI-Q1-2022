import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    #img = cv.imread('ufabc.png', cv.IMREAD_COLOR) 
    #img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = io.imread('..\\assets\\ufabc.png') 
    img_crop = img[:, 220:660]
    plt.figure(figsize = (15,5))
    #plt.imshow(img)
    plt.imshow(img_crop)
    plt.show()
    io.imwrite('ufabc_crop.png', img_crop)


if __name__ == '__main__':
    main()