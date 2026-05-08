import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read binary image
img = cv2.imread("binary.png", 0)

# Convert to binary (0 or 255)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Structuring elements
kernel1 = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]], dtype=np.uint8)

kernel2 = np.array([[1,0,1],
                    [0,0,0],
                    [1,0,1]], dtype=np.uint8)

# Erosion operations
erode1 = cv2.erode(binary, kernel1)
erode2 = cv2.erode(255 - binary, kernel2)

# Hit-or-Miss result
hmt = cv2.bitwise_and(erode1, erode2)

# Show results
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plt.title("Binary Image")
plt.imshow(binary, cmap='gray')

plt.subplot(1,2,2)
plt.title("HMT Result")
plt.imshow(hmt, cmap='gray')

plt.show()