from PIL import Image
import numpy as np

def main():
    im = Image.open("smallTestImage.png")
    print(im.format, im.size, im.mode)

    imageData = np.asarray(im)
    print("Iterating through pixel contents:")
    for x in range(len(imageData)):
        for y in range(len(imageData[x])):
            pixel = imageData[x][y]
            print(pixel)

main()
