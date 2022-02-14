import cv2

path_to_image = 'C:/Users/Natalie Fletcher/Dropbox (CSL)/Natalie Folder/Arden/Python/cat2.jpg'
image = cv2.imread(path_to_image)
cv2.resize(image, (100, 100))
cv2.imshow('image', image)
cv2.waitKey(0)

# You can load the image into grayscale using
#image = cv2.imread(path_to_image, 0) - replace line two with this line to greyscale

(B, G, R) = image[50, 50]
print("R = {}, G = {}, B = {}".format(R, G, B))

roi = image[100: 500, 200: 700]

import numpy as np
# Extract channels
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# Create empty images
blue_img = np.zeros(image.shape)
green_img = np.zeros(image.shape)
red_img = np.zeros(image.shape)

# Add colour to respective channel
blue_img[:, :, 0] = blue_channel / 255
green_img[:, :, 1] = green_channel / 255
red_img[:, :, 2] = red_channel / 255

# Combine channels
combined = blue_img + green_img + red_img

#Plot images
cv2.imshow('blue', blue_img)
cv2.imshow('green', green_img)
cv2.imshow('red', red_img)
cv2.imshow('combined', combined)

cv2.waitKey(0)

import numpy as np
import cv2

img = cv2.imread(path_to_image,0)
edges = cv2.Canny(img,100,200)


cv2.imshow('edges',edges)
cv2.imshow('image',img)

cv2.waitKey(0)

# capture frames from a camera

cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while (1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display an original image
    cv2.imshow('Original', frame)

    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)

    # Display edges in a frame
    cv2.imshow('Edges', edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break