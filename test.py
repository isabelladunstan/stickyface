import pixelate
from matplotlib import pyplot as plt
from matplotlib import image

for pixels in range(500,0,-100):
    pixelate.pixelate('_R000222.jpg', 'pixel.jpg', pixels)

    img = image.imread("pixel.jpg")
    plt.imshow(img)
    plt.show(block=False)
    plt.pause(0.001)

    sentence = "What is this image?\n1. Mountain\n2. Flowers\n3. Pretty Face\n\nChoose option or press enter to show more clearly: "

    a = input(sentence)

    plt.clf()