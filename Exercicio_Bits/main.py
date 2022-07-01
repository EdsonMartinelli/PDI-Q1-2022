import numpy as np

def main():
    bitsRGB = np.array([[ 1, 1, 1, 1, 1, 1, 1, 1],
                        [ 0, 0, 0, 0, 1, 1, 0, 1],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 1, 1, 1, 1, 1, 1, 1],
                        [ 0, 1, 1, 1, 1, 1, 1, 1],
                        [ 1, 1, 1, 1, 1, 1, 1, 1],
                        [ 0, 1, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 1, 0, 0, 0],
                        [ 1, 1, 0, 0, 0, 0, 0, 0]])

    print(tranform(bitsRGB))

def tranform(bitsRGB):
    height = bitsRGB.shape[0]
    arrayValues, bitValues = [], []
    for x in range(height):
        bitValues.append(binaryToDecimal(bitsRGB[x]))
        if((x + 1) % 3 == 0):
            arrayValues.append(bitValues)
            bitValues = []
    return arrayValues

def binaryToDecimal(binaryArray):
    decimalNumber = 0
    for x in range(len(binaryArray)):
        if(binaryArray[x] == 1):
            decimalNumber += np.power(2, len(binaryArray) - x - 1)
    return decimalNumber       

if __name__ == '__main__':
    main()