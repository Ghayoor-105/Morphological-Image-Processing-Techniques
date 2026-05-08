import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("binary.png", 0)

# Convert to binary
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Structuring element
kernel = np.ones((3, 3), np.uint8)

# Erosion
eroded = cv2.erode(binary, kernel)

# Boundary extraction
boundary = binary - eroded

# Show results
plt.figure(figsize=(8, 3))
plt.subplot(1, 3, 1)
plt.title("Binary Image")
plt.imshow(binary, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("Eroded Image")
plt.imshow(eroded, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Boundary")
plt.imshow(boundary, cmap='gray')

plt.show()