#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 13, 2024
#This program completes assignment 17

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size: "))
output_file = input("Enter output file: ")

purple = [128/255, 0, 128/255]
yellow = [1, 1, 0]

image = np.zeros((size, size, 3))

stripe_width = size // 10
for i in range(0, size, stripe_width*2):
    image[i:i+stripe_width, :, :] = purple
    if i+stripe_width < size:
        image[i+stripe_width:i+(stripe_width*2), :, :] = yellow

plt.imsave(output_file, image)

