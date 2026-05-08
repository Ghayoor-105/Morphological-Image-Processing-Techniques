import matplotlib.pyplot as plt
from skimage.morphology import skeletonize
from skimage.io import imread

# Read image
img = imread("binary.png", as_gray=True)

# Convert to binary
binary = img > 0.5

# Thinning (Skeletonization)
thinned = skeletonize(binary)

# Show results
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(binary, cmap='gray')

plt.subplot(1,2,2)
plt.title("Thinned Image")
plt.imshow(thinned, cmap='gray')

plt.show()