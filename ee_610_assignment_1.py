# -*- coding: utf-8 -*-
"""EE 610 Assignment 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qk9exSN4SurWKHBmT2njMsknjEye9JCb

**EE 610 Assignment 1**

**Question 1** 

**Image display**
"""

import cv2                #imported opencv library
from google.colab.patches import cv2_imshow   #cv2_imshow to display the image
img = cv2.imread("/content/B2DBy.jpg")       #read the image
cv2_imshow(img)                              #dispaly the image
print(img.shape)                             #prints the shape of image

"""**Shape of the image is (300, 332, 3) that represents:**

height of the input image is : 300 (represents the no. of pixel rows)

width of the input image is : 332 (represents the no. of pixel columns)

number of channels in the input image : 3 (Number of components used to represent each pixel)

**Question 2**

**Pixel Intensity values**
"""

h = img.shape[0]           #height of the input image
w = img.shape[1]           #width of the input image
(cx, cy) = (h//3, w//3)       # center of the image 
crop_img = img[0:cy, 0:cx]      #crop the main image keeping only the left corner
print("Top left corner of the image:")
cv2_imshow( crop_img)

#https://pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/

#to print the intensity of every pixel in the cropped image
for i in range(cx):        
  for j in range(cy):
    pixel = img[i,j]
    print(pixel)

"""The pixel intensity values are varying between 0 to 255 where 0 represents the darkest point and 255 corresponds to the brightest point.

Origin of the image is at (0,0) and then height is incrementing in the downwards direction and width in rightwards.

**Question 3**

**Overwriting pixel values with 255 in the copped image**
"""

for i in range(cx):
  for j in range(cy):
    img[i,j] = [255,255,255]                        #converts the intensity of all pixels in this range to 255
    cv2_imshow(img)

"""Since the intensities in the cropped are overwritten by 255 and 255 represents the brightest part/ white color in greyscale images. Here in the cropped part has turned brighter/white.

**Question 4**

**Overwriting intensity values with 256**
"""

for i in range(cx):
  for j in range(cy):
    img[i,j] = [256,256,256]                #converts the intensity of all pixels in this range to 256
cv2_imshow(img)

"""in greyscale images, pixel values lies in range 0 to 255 where 0 corresponds to "black" and 1 corresponds to "white". Here 256 represents 0 intensity which corresponds to black color. Hence, this part has turned black.

**Question 5**

**Display of an image cropped from all four sides**
"""

h_a = h//8                #divides h by 8 
h_b = 7*h//8              
w_a = w//8
w_b = 7*w//8
img = cv2.imread("/content/B2DBy.jpg")   #read the image the image
cropped_img = img[w_a:w_b, h_a:h_b]      #crop the 1/8th size of image form all four corners
cv2_imshow(cropped_img)                  #display image

"""**Question 6**

**Saving image as a new file in png format**
"""

cv2.imwrite('/content/edited_img.png',cropped_img)         #writes the image to the specified path

"""**Question 7**

**Increasing all pixel values of original image by 50**
"""

for i in range(h):                          #running the loop over all pixles
  for j in range(w):
    img[i,j] = img[i,j]+[50,50,50]                #added 50 to all pixel values 
cv2_imshow(img)                                    #display image

"""After increasing pixel values by 50, some points have been drakened and some has become brighter. Pixels that were closer to 0, have become a bit brighter and pixels that were closer to 255, have become dark as these values now corresponds to closer values of 0. Hence, this pixels have become dark.

**Question 8**

**Mirror image**
"""

img = cv2.imread("/content/B2DBy.jpg")   #read the image the image
print("original image:")
cv2_imshow(img)
image = cv2.flip(img, 1)            #inverts y-axis to get mirror image
#res = result = np.hstack((img, image))       #to stack image side by side
print("mirror image:")
cv2_imshow(image)                   #display image

"""**Question 9**

**Greyscale imaging and histogram display**

"""

night_shot = cv2.imread("/content/135-copy_orig.jpg")     #read the image
print("Night shot image:")
cv2_imshow(night_shot)      #display the night shot image

gray_image = cv2.cvtColor(night_shot, cv2.COLOR_BGR2GRAY)     #converts the pic to gray scale

print("Gray scale image:")
cv2_imshow(gray_image)

from matplotlib import pyplot as plt
hist = cv2.calcHist([gray_image], [0], None, [256], [0,256])            #calculates histogram
plt.plot(hist)                                                           #plot histogram
plt.title("Grayscale Histogram")             #title of the plot
plt.xlabel("Bins")                            # x label of plot
plt.ylabel("# of Pixels")

"""**Question 10**"""

height = night_shot.shape[0]                  #height of the night_shot image
width = night_shot.shape[1]                   #width of the night_shot image
print(night_shot.shape)
#loop for multiplying every pixel with a
a=2
gray_image = cv2.cvtColor(night_shot, cv2.COLOR_BGR2GRAY)       #converts to grey scale
for i in range(height):
  for j in range(width):
    gray_image[i,j] = gray_image[i,j]*a                         #increases the pixel intensity by multiple of a 
cv2_imshow(gray_image)

"""**Question 11**

**Power Transform**
"""

import numpy as np
night_shot = cv2.imread("/content/135-copy_orig.jpg")     #read the image
gray_image = cv2.cvtColor(night_shot, cv2.COLOR_BGR2GRAY)    #to restore the grey scale image

#different gamma values
for gamma in [0.1,0.3,0.4,0.5,0.8,0.9,1.2,2.2]:
  #to apply gamma correction
  gamma_corrected = np.array(255*(gray_image / 255) ** gamma, dtype = 'uint8')
  print('gamma:', str(gamma))
  cv2_imshow(gamma_corrected)


#source:https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/

"""Gamma values less than 1 are brightening dark areas whereas gamma values greater than 1 are enhancing the brightness of brighter portions. Though the best gamma value is depend on the requirement of the image. In this image, gamma = 0.5 is giving satisfactory results.

**Question 12**

**Histogram Equalization**
"""

gray_image = cv2.cvtColor(night_shot, cv2.COLOR_BGR2GRAY)    #to restore the grey scale image
#histogram equalization
equ_img = cv2.equalizeHist(gray_image)
result = np.hstack((gray_image, equ_img))       #to stack image side by side
  
cv2_imshow(result)                             #to print images

#histogram curve of the equalized histogram image
hist = cv2.calcHist([hist_equ_img], [0], None, [256], [0,256])         #to find histogram
plt.plot(hist)                                         #plots histogram
plt.title("Eqalized Histogram")                  #title of histogram plot
plt.xlabel("Bins")                               #label of x-axis
plt.ylabel("# of Pixels")                         #label of y-axis

"""Histogram plot after equalization is not flat because during histogram equalization, we use a discrete sum to approximate a continuous integral of the cumulative PDF of the pixels. This maps pixels with different values in the original image to the same value in equalized histogram.

**Question 13**

**Histogram Matching**
"""

ref_image = cv2.imread("/content/images (1).jfif")  
print("Reference image:")
cv2_imshow(ref_image)
print('No of Channel in reference image is: ' + str(ref_image.shape[2])) # checking the number of channels

night_shot = cv2.imread("/content/135-copy_orig.jpg")     #read the image
print("Input image:")
cv2_imshow(night_shot)
print('No of Channel in input image is: ' + str(night_shot.shape[2])) # checking the number of channels

# import packages
from skimage import exposure
from skimage.exposure import match_histograms
  
matched = match_histograms(night_shot, ref_image, multichannel=True,)       #matching histograms
cv2_imshow(matched)                                               #show matched image

#source:https://www.geeksforgeeks.org/histogram-matching-with-opencv-scikit-image-and-python/

#histogram of these images
hist_ref = cv2.calcHist([ref_image], [0], None, [256], [0,256])         #to find histogram
plt.plot(hist_ref)                                                      #plot histogram

hist_source = cv2.calcHist([night_shot], [0], None, [256], [0,256])         #to find histogram
plt.plot(hist_source)                                                  #plot histogram

hist_matched = cv2.calcHist([matched], [0], None, [256], [0,256])         #to find histogram
plt.plot(hist_matched)          #plot histogram

