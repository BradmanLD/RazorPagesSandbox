from PIL import Image
import numpy as np

def main():
    im = Image.open("smallTestImage.png")
    print(im.format, im.size, im.mode)

    pixelMatrix = get_pixel_matrix(im)
    """
    for testing pixel matrix
    for row in pixelMatrix:
        for pixel in row:
            print(pixel)
    """

def get_pixel_matrix(img):
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

main()
