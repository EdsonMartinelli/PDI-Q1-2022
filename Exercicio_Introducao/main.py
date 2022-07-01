import numpy as np
import imageio as io

def main():
    imgLogo = io.imread('..\\assets\\ufabc.png') 
    imgSA = io.imread('..\\assets\\campus-sa.jpg') 
    imgSBC = io.imread('..\\assets\\campus-sbc.jpg') 

    widthDiff = np.shape(imgLogo)[1] - np.shape(imgSA)[1]
    cutSize = int(widthDiff / 2)
    imgLogo_Crop = imgLogo[:, cutSize : np.shape(imgLogo)[1] - cutSize]
    imgLogo_Crop_Flip = np.fliplr(imgLogo_Crop)


    heightLogo = np.shape(imgLogo_Crop)[0]
    heightCampus = np.shape(imgSA)[0]
    height = heightLogo + heightCampus
    width = np.shape(imgLogo_Crop)[1] * 2
    result = np.zeros((height, width, 3), dtype = np.uint8)

    result[: heightLogo, 0 : int(width / 2)] = imgLogo_Crop
    result[: heightLogo, int(width / 2) : width] = imgLogo_Crop_Flip
    result[heightLogo : height, 0: int(width / 2) ] = imgSA
    result[heightLogo : height, int(width / 2): width] = imgSBC

    io.imwrite('result.png',result)


if __name__ == '__main__':
    main()