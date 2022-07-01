import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    img = io.imread('..\\assets\\ufabc.png') 
    imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary_image = cv.threshold(imgGray, 127, 255, cv.THRESH_BINARY)

    A = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)


    B = np.ones((3, 3), np.uint8) 

    print(testOpening(A, B))
    print(testClosing(A, B))

    fig = plt.figure(figsize = (8, 8))

    ax1 = fig.add_subplot(3, 2, 1)
    ax1.set_title("Erode")
    erodeAB = cv.erode(A, B)
    plt.imshow(erodeAB, cmap='gray', vmin=0, vmax=1)

    ax2 = fig.add_subplot(3, 2, 2)
    ax2.set_title("Dilate")
    dilateAB = cv.dilate(A, B)
    plt.imshow(dilateAB, cmap='gray', vmin=0, vmax=1)

    ax3 = fig.add_subplot(3, 2, 3)
    ax3.set_title("Opening")
    openingAB = opening(A, B)
    plt.imshow(openingAB, cmap='gray', vmin=0, vmax=1)

    ax4 = fig.add_subplot(3, 2, 4)
    ax4.set_title("Closing")
    closingAB = closing(A, B)
    plt.imshow(closingAB, cmap='gray', vmin=0, vmax=1)

    ax5 = fig.add_subplot(3, 2, 5)
    ax5.set_title("Image_Test Opening")
    testImageOpening = opening(binary_image, B)
    plt.imshow(testImageOpening , cmap='gray', vmin=0, vmax=1)

    ax5 = fig.add_subplot(3, 2, 6)
    ax5.set_title("Image_Test Closing")
    testImageClosing = closing(binary_image, B)
    plt.imshow(testImageClosing , cmap='gray', vmin=0, vmax=1)

    plt.show()

def opening(A,B):
    return cv.dilate(cv.erode(A, B), B)

def closing(A,B):
    return cv.erode(cv.dilate(A, B), B)

def testOpening(A, B):
    openingAB_test = opening(A,B)
    openingAB_CV =  cv.morphologyEx(A, cv.MORPH_OPEN, B)
    return np.array_equal( openingAB_test, openingAB_CV)

def testClosing(A, B):
    closingAB_test = closing(A,B)
    closingAB_CV =  cv.morphologyEx(A, cv.MORPH_CLOSE, B)
    return np.array_equal( closingAB_test, closingAB_CV)

if __name__ == '__main__':
    main()