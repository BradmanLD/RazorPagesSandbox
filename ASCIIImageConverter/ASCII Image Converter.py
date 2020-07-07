from PIL import Image

def main():
    im = Image.open("testImage.jpg")
    print(im.format, im.size, im.mode)

main()
