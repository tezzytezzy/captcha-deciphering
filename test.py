import cv2
import numpy as np
from constants import * # Retrieve FILE_NAME

# Change this to one of your generated images:
#image_file = 'example.png' 
image_file = FILE_NAME

image = cv2.imread(image_file)
cv2.imshow('Original image', image)

# Convert to grayscale, followed by thresholding to black and white
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow('Black and white', thresh)

# Apply opening: "erosion" followed by "dilation"
# The basic idea of erosion is just like soil erosion : this transformation 
#  “erodes away” boundaries of the foreground object (which is assumed to be 
#  in white) by sliding a “kernel” over the image (a “window,” so to speak) 
#  so that only those white pixels are retained if all pixels in the surrounding
#  kernel are white as well. Otherwise, it gets turned to black.
# Dilation does the opposite: it widens the image by setting pixels to white 
#  if at least one pixel in the surrounding kernel was white.
# The kernel sizes used in the script above are simply the result of 
#  some trial and error, and adjust these with other types of CAPTCHA images.
# Note that we allow for some noise in the image to remain present. We don’t need
#  to obtain a perfect image as we trust that our predictive model will be able
#  to “look over these.”
denoised = thresh.copy()
kernel = np.ones((4, 3), np.uint8)
denoised = cv2.erode(denoised, kernel, iterations=1)
kernel = np.ones((6, 3), np.uint8)
denoised = cv2.dilate(denoised, kernel, iterations=1)
cv2.imshow('Denoised', denoised)

# Now find contours and overlay them over our original image
# Next, we use OpenCV’s findContours method to extract “blobs” of connected white pixels.
cnts, _ = cv2.findContours(denoised.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contoured = image.copy()
cv2.drawContours(contoured, cnts, contourIdx=-1, color=(255, 0, 0), thickness=-1)
# To draw the discovered blobs.
#  contourIdx=-1: draw all top-level contours
#  thickness=-1: fill up the contours

cv2.imshow('Contours', contoured)

# Create a fresh 'mask' image
mask = np.ones((image.shape[0], image.shape[1]), dtype="uint8") * 0
# We'll use the first contour as an example
contour = cnts[0]
# Draw this contour over the mask
# I.e., Take one contour and draw it in white on top of this “mask.”
cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

cv2.imshow('Denoised image', denoised)
cv2.imshow('Mask after drawing contour', mask)

result = cv2.bitwise_and(denoised, mask)
# The denoised image and mask are combined in a bitwise “and” operation, which will 
#  retain white pixels if the corresponding pixels in both input images were white, 
#  and sets it to black otherwise.

cv2.imshow('Result after and operation', result)

retain = result > 0
result = result[np.ix_(retain.any(1), retain.any(0))]
# Apply some clever numpy slicing to crop the image.

cv2.imshow('Final result', result)

cv2.waitKey(0)
