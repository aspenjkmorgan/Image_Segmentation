# TITLE: Example I/O for Software Assignment #2
# CLASS: CSCI 332, Fall 2023
# Author: Aspen Morgan
# Date: 2023.12.13
# Collaborated (conceptually) with Jayce Holdsambeck

import segmentationClass
import numpy as np
from matplotlib import pyplot as plt 
from PIL import Image

# initialize an object 
obj = segmentationClass.segmentationClass()

# import in image
img = Image.open('spiral.png')
arr = np.array(img)

# set object properties
obj.x_a = np.array([0,0]) 
obj.x_b = np.array([0,9])  
obj.p0 = 1

# print requested rows 
A = obj.constructAdjacencyMatrix(arr)
print(A[[0,10],:])

# segment the image
t = obj.segmentImage(arr)

# Plot the results
fig, axs = plt.subplots(1,2)
fig.suptitle('Input and segmentation')
axs[0].imshow(arr.astype(np.uint8), interpolation='nearest')
axs[0].set_title("Input image (3x3)")
axs[1].imshow(255*t.astype(np.uint8), interpolation='nearest', cmap='gray')
axs[1].set_title("Binary segmentation")
plt.show()