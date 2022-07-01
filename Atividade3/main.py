import cv2 as cv
import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    img = io.imread('..\\assets\\forms.jpeg') 
    imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary_image = cv.threshold(imgGray, 127, 255, cv.THRESH_BINARY_INV)

    kernel1 = np.ones((9,9),np.uint8)
    kernel2 = np.ones((3,3),np.uint8)

    img1=cv.dilate(binary_image, kernel1, iterations=3)
    img2=cv.erode(img1, kernel2, iterations=1)
   
    contours, hierarchy = cv.findContours(img2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    newCont= getCorrectContours(contours, hierarchy)
    withContours =  cv.drawContours(img, newCont, -1, (0,255,0), 10)

    blackImage = np.zeros(binary_image.shape, np.uint8)
    onlyPolygons = cv.drawContours(blackImage, newCont, -1, (255,255,255), cv.FILLED)

    withDetectImage = cv.drawContours(img, newCont, -1, (0,255,0), 10)
    withNumbers = sizeOfPolygon(newCont, withDetectImage, onlyPolygons)

    fig = plt.figure(figsize = (15,5))

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_title("Normal")
    plt.imshow(binary_image, cmap='gray', vmin=0, vmax=255)

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_title("Normal")
    plt.imshow(withContours, cmap='gray', vmin=0, vmax=255)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_title("Erode")
    plt.imshow (onlyPolygons, cmap='gray', vmin=0, vmax=255)

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.set_title("Erode")
    plt.imshow (withNumbers, cmap='gray', vmin=0, vmax=255)
    plt.show()


def getCorrectContours(contours, hierarchy):
    newContours = []
    for x in range(len(contours)):
        if(hierarchy[0][x][2] == -1):
            newContours.append(contours[x])
    return newContours

def sizeOfPolygon(contours, image, onlyPolygons):
    newImage = np.copy(image)
    for x in range(len(contours)):
        moment=cv.moments(contours[x]) 
        cx = int(moment['m10'] / moment['m00']) 
        cy = int(moment['m01'] / moment['m00']) 
        cv.putText(newImage, 
                   getSize(contours[x], onlyPolygons),
                   (cx-50,cy),
                   cv.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),2)
    return newImage

def getSize(contour, onlyPolygons):
    x, y, w, h = cv.boundingRect(contour)
    pixels = cv.countNonZero(onlyPolygons[y : y + h, x : x + w])
    return str(pixels)

if __name__ == '__main__':
    main()