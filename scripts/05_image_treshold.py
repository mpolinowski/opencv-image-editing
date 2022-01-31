import cv2
import numpy as np

image = cv2.imread('resources/test-image.jpg', cv2.IMREAD_GRAYSCALE)

# Set threshold and maxValue
thresh = 127
maxValue = 255

ret, thresh_binary = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh_binary)

ret, thresh_binary_inv = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverted", thresh_binary_inv)

ret, thresh_trunc = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TRUNC)
cv2.imshow("Threshold Truncated", thresh_trunc)

ret, thresh_tozero = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO)
cv2.imshow("Threshold toZero", thresh_tozero)

ret, thresh_tozero_inv = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO_INV)
cv2.imshow("Threshold toZero Inverted", thresh_tozero_inv)


# Canny Edge Detection
canny_image_src = cv2.Canny(image, 85, 255)
canny_image = cv2.Canny(thresh_binary, 85, 255)

cv2.imshow("Canny Image from Source", canny_image_src)
cv2.imshow("Canny Image", canny_image)

cv2.waitKey(5000)
cv2.destroyAllWindows()
