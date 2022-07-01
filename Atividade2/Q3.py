import cv2 as cv
import numpy as np

def main():
    input = np.array([[5,7,7,1,3,5,1,3,1,5,1,5],
                      [1,5,3,1,3,1,5,1,1,1,1,5],
                      [7,5,1,7,1,7,3,3,3,5,1,1],
                      [5,5,5,3,5,3,5,1,5,1,7,3],
                      [3,3,3,1,5,5,1,7,3,1,3,1],
                      [3,1,3,3,3,1,1,1,3,1,5,1],
                      [5,1,5,1,5,1,1,3,1,7,5,7],
                      [1,5,5,3,7,3,1,1,1,5,3,5],
                      [5,3,1,7,1,5,1,1,5,3,1,1],
                      [3,3,5,1,5,1,3,1,1,5,1,1],
                      [5,1,5,1,1,1,7,7,3,3,5,7],
                      [5,3,1,5,7,1,3,1,3,3,3,3],
                      [5,7,1,1,3,1,1,3,3,1,1,3]], np.uint8)

                  
    kernel = np.ones((1,1,0,1,1,0,1), np.uint8)

    output = cv.dilate(cv.erode(input, kernel), kernel)
    compare_output= cv.morphologyEx(input, cv.MORPH_OPEN, kernel)
    print(output)

if __name__ == '__main__':
    main()