import numpy as np
import imageio as io
import matplotlib.pyplot as plt

def main():
    norte = np.array([255, 0  , 0  ])
    sul =   np.array([0  , 0  , 255])
    leste = np.array([0  , 255, 0  ])
    oeste = np.array([127, 127, 127])
    height, width = 5, 5
    result = np.zeros((height, width, 3), dtype=np.uint8)

    result[0][0] = color_overlay(norte, oeste)
    result[0][int(width / 2)] = norte
    result[0][width - 1] = color_overlay(norte, leste)
    result[int(height / 2)][0] = oeste
    result[int(height / 2)][width - 1] = leste
    result[height - 1][0] = color_overlay(sul, oeste)
    result[height - 1][int(width / 2)] = sul
    result[height - 1][width - 1] = color_overlay(sul, leste)

    plt.figure(figsize = (8,8))
    plt.imshow(result)
    plt.show()
    io.imwrite('result.png', result)


def color_overlay(color1, color2):
    newColor = np.array([0, 0, 0])
    for x in range(3):
        newColor[x] = color1[x] + color2[x]
        if(newColor[x] > 255):
            newColor[x] = 255
    return newColor


if __name__ == '__main__':
    main()