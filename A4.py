'''Program: Assignment4
Do some simple image processing.
Written by David Johnson and Preston Little
This code, or derived works, may not be publicly posted.
'''

# This brings in functions from the graphics.py file
from graphics import *
# We will need some random numbers
from random import randrange

# This function makes a new image that moves the red intensity value of a pixel to the green
# part of a pixel, moves the green value to blue, and the blue value to red. An image that had
# a bright green part will end up with that part being bright blue in the new image.
#
# Study the pattern of the loop inside a loop (called nested loops). Each time the first loop
# does a single repeat, the entire inner loop does all its repetitions.
#
# Look how to get the color at a pixel, change the color, and set the pixel to the new color.
# The assignment problems below will use these steps.

# This function returns a new image with changed colors. The code in main calls
# this function and draws the returned new image.
# The function is fully-implemented and should not be modified.
def switch_image_colors(image):
    switched_image = image.clone()  # copy the image
    # go across the image with the for x loop and then move down a row
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Get the red, green, and blue intensity values
            red_color = image.getPixelRed(x, y)  # get the pixel color
            green_color = image.getPixelGreen(x, y)  # get the pixel color
            blue_color = image.getPixelBlue(x, y)  # get the pixel color
            # Set the pixel in the new image to have the swapped around intensity values
            switched_image.setPixelRed(x, y, green_color)  # Set the pixel to the new color
            switched_image.setPixelGreen(x, y, blue_color)  # Set the pixel to the new color
            switched_image.setPixelBlue(x, y, red_color)  # Set the pixel to the new color
    return switched_image  # return the finished new image

# Make a function that sets every pixel of a new image to a gray version of
# the same positioned pixel in the original image.
# A gray color can be computed by finding the average
# of the red, green, and blue parts of the original pixel and assigning that
# average to the red, green, and blue parts of the new image.
#
# The average calculated is summing the red, green, and blue values and dividing by 3.
# After dividing by 3, use the int conversion function to make it an integer value,
# which is the form of number the Image object uses.
#
# The function should follow the pattern of the example above:
#   - clone the function parameter
#   - loop over the image x and y coordinates
#   - get the red, green, and blue values
#   - assign new values to the cloned image red, green, and blue values.
#   - return the changed image
def color_image_to_gray_scale(image):
    gray_image = image.clone()
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            red_color = image.getPixelRed(x, y)
            green_color = image.getPixelGreen(x, y)
            blue_color = image.getPixelBlue(x, y)

            average = (red_color + green_color + blue_color) / 3

            gray_image.setPixelRed(x, y, int(average))
            gray_image.setPixelGreen(x, y, int(average))
            gray_image.setPixelBlue(x, y, int(average))
    return gray_image


# Make a function that makes a photonegative of the original.
# The red value should be set to 255 - original red, green to 255 - original green
# and the same for the blue value. Return the changed image.
def photonegative_of_an_image(image):
    photonegative_image = image.clone()
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            red_color = image.getPixelRed(x, y)
            green_color = image.getPixelGreen(x, y)
            blue_color = image.getPixelBlue(x, y)

            red_photonegative = (255 - red_color)
            green_photonegative = (255 - green_color)
            blue_photonegative = (255 - blue_color)

            photonegative_image.setPixelRed(x, y, red_photonegative)
            photonegative_image.setPixelGreen(x, y, green_photonegative)
            photonegative_image.setPixelBlue(x, y, blue_photonegative)

    return photonegative_image

# Make a function that brightens the original. To do this, multiply each color
# value by 2. Some values * 2 will be larger than the allowed 0-255 range for a color.
# The graphics module sets all values bigger than 255 to 255 to keep values in that range.
# Return the changed image.
def brighten_image(image):
    brightened_image = image.clone()
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            red_color = image.getPixelRed(x, y)
            green_color = image.getPixelGreen(x, y)
            blue_color = image.getPixelBlue(x, y)

            red_brightened = red_color * 2
            green_brightened = green_color * 2
            blue_brightened = blue_color * 2

            brightened_image.setPixelRed(x, y, red_brightened)
            brightened_image.setPixelGreen(x, y, green_brightened)
            brightened_image.setPixelBlue(x, y, blue_brightened)

    return brightened_image


# Make a function that merges two image. The logic here is the same as used in
# green screen technology from special effects.
#
# The green image is mostly pure green (0, 255, 0) but has a cat in it (where the pixels are not green).
# The background image is just a nice image that is the same size as the green image.
# First, clone the green image to start the merged image.
# At each pixel location of the cloned merged image, check the pixel color.
# If the pixel is pure green (so the red is 0, the green is 255, and the blue is 0)
# assign the color of the background pixel to the merged image. If it the pixel is not pure green, do nothing
# (this leaves the cat in the image).
# Return the merged image.
def green_screen_image(green_image, background_image):
    merged_image = green_image.clone()
    for y in range(0, green_image.getHeight()):
        for x in range(0, green_image.getWidth()):
            red_color = green_image.getPixelRed(x, y)
            green_color = green_image.getPixelGreen(x, y)
            blue_color = green_image.getPixelBlue(x, y)

            green_screen_red = background_image.getPixelRed(x, y)
            green_screen_green = background_image.getPixelGreen(x, y)
            green_screen_blue = background_image.getPixelBlue(x, y)

            if red_color == 0 and green_color == 255 and blue_color == 0:
                merged_image.setPixelRed(x, y, green_screen_red)
                merged_image.setPixelGreen(x, y, green_screen_green)
                merged_image.setPixelBlue(x, y, green_screen_blue)

    return merged_image

# Make a function that randomly picks a pixel location, finds the color
# at that location, and draws a circle at that location filled with that color onto the
# window. The function should do this finding and drawing process 50000 times.
# This will cover the old image with a artistic style.
# You need to pick an x location from 0 to one less than the image width (inclusive).
# You need a y location from 0 to one less than the image height (inclusive).
# Review the lab that used a random number to aid your development of this code.
# This function is not like the ones above in that we are not examining and changing every pixel
# in an image. Those functions used nested loops to accomplish that. This function does one kind
# of task (picking a random pixel and drawing a circle) 50,000 times. Consider what kind of
# loop would be best suited for this task.
#
# An example of drawing a circle to image is
#
#         circle = Circle(Point(x, y), 5) # 5 makes a 5 pixel radius circle and x,y is the center
#         circle.setFill(red_color, green_color, blue_color)
#         circle.setWidth(0) # This gets rid of the circle border
#         circle.draw(win)
#
def color_image_to_pointillist(image, win):
    pointillist_image = image.clone()
    for i in range(50000):
        y = randrange(0, image.getHeight() - 1)
        x = randrange(0, image.getWidth() - 1)

        red_color = image.getPixelRed(x, y)
        green_color = image.getPixelGreen(x, y)
        blue_color = image.getPixelBlue(x, y)

        circle = Circle(Point(x, y), 5)
        circle.setFill(red_color, green_color, blue_color)
        circle.setWidth(0)
        circle.draw(win)

    return pointillist_image

# This function loads the image file and centers it in the window. The image is returned so
# it can be drawn. You should not modify it.
def load_image(filename):
    # Load the image
    image = Image(Point(0, 0), filename)
    # Center it
    image.move(int(image.getWidth()/2), int(image.getHeight()/2))
    return image

# Main loads images, opens a window, and calls each of the image processing functions and displays the result.
def main():
    # Load the image first so we know how big to make the window.

    arches_image = load_image("Arches.png")
    cat_image = load_image("green-screen-cat.png")

    # Setup the window using the image size
    win = GraphWin('Image Art', arches_image.getWidth(), arches_image.getHeight(), autoflush=False)
    win.setBackground('yellow')  # This is here to help see if the image is centered.

    # Draw the original image and wait for a mouse click to move to the next step
    arches_image.draw(win)
    win.getMouse()

    # Make a new image with green intensity put in red, blue put in green, and red in blue.
    switched_image = switch_image_colors(arches_image)
    switched_image.draw(win)
    win.getMouse()

    # As you implement the functions above, uncomment these lines to test the functions.
    #
    # # Test the grayscale
    gray_image = color_image_to_gray_scale(arches_image)
    gray_image.draw(win)
    gray_image.save("gray.png")
    win.getMouse()
    #
    # # Test the photonegative
    photonegative_image = photonegative_of_an_image(arches_image)
    photonegative_image.draw(win)
    photonegative_image.save("photonegative.png")
    win.getMouse()
    #
    # # Test the brighten
    brightened_image = brighten_image(arches_image)
    brightened_image.draw(win)
    brightened_image.save("brightened.png")
    win.getMouse()
    #
    # # Make a merged image between a green screen image and a background
    merged_image = green_screen_image(cat_image, arches_image)
    merged_image.draw(win)
    merged_image.save("merged.png")
    win.getMouse()
    #
    # # Test the pointillist function. It is just drawn on the window. You will need to
    # # screen capture the image to save it for submitting.
    color_image_to_pointillist(arches_image, win)
    win.getMouse()

    win.close()

# Execute main when this file is run.


if __name__ == "__main__":
    main()
