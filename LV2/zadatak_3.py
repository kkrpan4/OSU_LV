import numpy as np 
import matplotlib.pyplot as plt
import cv2


img = plt.imread("road.jpg")
copy = img.copy()

alpha = 1.5 # Contrast control
beta = 10 # Brightness control

# call convertScaleAbs function
adjusted = cv2.convertScaleAbs(img, alpha, beta)

# display the output image
cv2.imshow('adjusted', adjusted)