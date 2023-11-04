import pixelate
from matplotlib import pyplot as plt
from matplotlib import image
import random 

labels = ['Mountain', 'Flower', 'Ramen', 'Cake', 'Dog']
img_folder = 'Images/'
img_names = ['mountain.jpg', 'flower.jpg', 'ramen.jpg', 'cake.jpg', 'dog.jpg']

plt.ion()  # Turn on interactive mode


choice=random.randint(0,4)
img_name=img_folder+img_names[choice]

for pixels in range(501,0,-100):
    pixelate.pixelate(img_name, 'pixel.jpg', pixels)

    img = image.imread("pixel.jpg")
    plt.imshow(img)
    plt.draw()  # Update the plot
    plt.show()

    sentence = "What is this image?\n1. Mountain\n2. Flowers\n3. Ramen\n4. Cake\n5. Dog\n\nChoose option or press enter to show more clearly: "

    a = input(sentence)

    plt.clf()

plt.ioff()  # Turn off interactive mode after loop ends