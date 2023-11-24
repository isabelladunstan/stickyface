# Packages
import pixelate
from matplotlib import pyplot as plt
from matplotlib import image
import random 

# Naming conventions
img_folder = 'Images/'
img_names = ['mountain.jpg', 'flower.jpg', 'ramen.jpg', 'cake.jpg', 'dog.jpg']

plt.ion()  # Turn on interactive mode - means when I show the image it will keep updating

# Randomising images as they appear in program
choice=random.randint(0,4)
randomimage=img_folder+img_names[choice]
# Correct image congratulations 
winnerimg=img_folder+'Winner.png'
# Loop pixelating images
# The zero is the limit of the loop i.e. can't go lower
for pixels in range(501,0,-100):
   
    pixelate.pixelate(randomimage, 'pixel.jpg', pixels)

    sentence = "What is this image?\n1. Mountain\n2. Flowers\n3. Ramen\n4. Cake\n5. Dog\n\nChoose an option or press enter to show the image more clearly. To exit press 0: "

    # Reading the pixelated image
    img = image.imread("pixel.jpg")
    # Display image
    plt.imshow(img)
    plt.draw()  # Update the plot
    plt.show()

    # Function 'input' = wanting the user to put something into the terminal, and tell them what they can input using the question (sentence)
    a = input(sentence)

    # User choices - conditional statements 
    if choice==0 and a=='1':
        print('\nCorrect!')
        fullimage=image.imread(randomimage)
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input('Press Enter!')
        fullimage=image.imread(winnerimg) 
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input()
        break 
    elif choice==1 and a=='2':
        print('\nCorrect!')
        fullimage=image.imread(randomimage) 
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input('Press Enter!')
        fullimage=image.imread(winnerimg) 
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input()
        break 
    elif choice==2 and a=='3':
        print('\nCorrect!')
        fullimage=image.imread(randomimage)
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input('Press Enter!')
        fullimage=image.imread(winnerimg) 
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input()
        break 
    elif choice==3 and a=='4':
        print('\nCorrect!')
        fullimage=image.imread(randomimage)
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input('Press Enter!')
        fullimage=image.imread(winnerimg) 
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input()
        break 
    elif choice==4 and a=='5':
        print('\nCorrect!')
        fullimage=image.imread(randomimage)
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input('Press Enter!')
        fullimage=image.imread(winnerimg) 
        # Display image
        plt.imshow(fullimage)
        plt.draw()  
        plt.show()
        # stop the loop once guess is correct
        a=input()
        break 
    elif a=='0':
        print('\nGoodbye world!')
        plt.close()
        break
    # Wrong answer
    else:
        print('\nWrong!')

    plt.clf()

plt.ioff()  # Turn off interactive mode after loop ends