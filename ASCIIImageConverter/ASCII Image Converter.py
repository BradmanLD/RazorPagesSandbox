from PIL import Image
import numpy as np
ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


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
    brightnessMatrix = convert_rgb_to_brightness(pixelMatrix)

def get_pixel_matrix(img):
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def convert_rgb_to_brightness(pixelMatrix):
    # Keep strucutre of the matrix the same but replace the RGB information with
    # averaged brightness. Future: add luminosity / lumanince options.
    brightnessMatrix = []
    for row in pixelMatrix:
        brightnessRow = []
        for pixel in row:
            brightness = (pixel[0] + pixel[1] + pixel[2]) / 3.0
            brightnessRow.append(brightness)
        brightnessMatrix.append(brightnessRow)
    return brightnessMatrix

main()
