import cv2
import numpy as np

image = cv2.imread('resources/test-image.jpg')

# Sharpening
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.imwrite("processed/sharpened_image.jpg", sharpened_image)


# Blurring
kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

blurred_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Blurred Image", blurred_image)
cv2.imwrite("processed/blurred_image.jpg", blurred_image)

# Outlining
kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

outlined_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Outlined Image", outlined_image)
cv2.imwrite("processed/outlined_image.jpg", outlined_image)

# Embossing
kernel = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
])

embossed_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Embossed Image", embossed_image)
cv2.imwrite("processed/embossed_image.jpg", embossed_image)


# Sobel Filter
kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobel_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Sobel Filter", sobel_image)
cv2.imwrite("processed/sobel_image.jpg", sobel_image)


cv2.waitKey(35000)
cv2.destroyAllWindows()