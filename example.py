# TITLE: Example I/O for Software Assignment #2
# CLASS: CSCI 332, Fall 2023
# Author: Jordan Malof
# Date: 2023.12.08
# VERSION 2

#Import your class (it should be in same directly as this file)
import segmentationClass

#Import numpy, and plotting package
import numpy as np
from matplotlib import pyplot as plt

#Instantiate an object for your class. 
obj = segmentationClass.segmentationClass()

## Create a simple test image
# The image has two red pixels, and other pixels are zero-valued
# Note: for your test script you should import png image (e.g.,  using Pillow)
I = np.zeros([3,3,3]);
I[2,2,0]=128;
I[1,2,0]=128;


#Set segmentation object properties 
obj.x_a = np.array([2,2]);  # Foreground pixel coordinate
obj.x_b = np.array([0,0]);  # Background pixel coordinate
obj.p0 = 1;                # Edge capacities between neighboring pixels

# Segment the image
# This method and its I/O are needed in your implementaiton
t = obj.segmentImage(I);

# Plot the results
fig, axs = plt.subplots(1,2)
fig.suptitle('Input and segmentation')
axs[0].imshow(I.astype(np.uint8), interpolation='nearest')
axs[0].set_title("Input image (3x3)")
# The matrix 't' is binary, but it is helpful to scale the values to be 0 or 255
#  when displaying with imshow
axs[1].imshow(255*t.astype(np.uint8), interpolation='nearest')
axs[1].set_title("Binary segmentation")
plt.show()


# # Return the adjacency matrix for the graph representing the image
# note: In my implementation, I work with adjacency *lists* internally because it is much faster. 
# Therefore inside this function I convert my adjacency list to an adjacency matrix 
# Inspecting your adjacency matrix is a useful debugging step 
A = obj.constructAdjacencyMatrix(I)

# Display adjacency matrix for pixels at location (0,0) and (1,0) 
# In a 3x3 image, this corresponds to rows 0 and 3 in an adjacency matrix
# You are *required* to display an adjacency matrix for these two pixels, although
# the precise way in which you do it is up to you. Some additional notes
# 1) The order of the columns could be different than mine, but the numbers should be the same.  
# In other words, in the first row below, you should always have three values of "1" and one value of "442"
# but they could be in different columns than shown here.    
# 2) In my example here, the last two columns of my adjacency matrix represent a source and target node, respectively. 
# print(A[[0,3],:])