import cv2

image = cv2.imread('resources/test-image.jpg')

# Read pixel value
pixel = image[100, 100]
print(pixel)

redValue = image[100, 100, 2]
print(redValue)

# Change pixel value
whitePixel = image[100, 100] = [255, 255, 255]
print(whitePixel)

# Image Properties
print('Image shape: ', image.shape)
print('Image data type: ', image.dtype)
print('Image size: ', image.size)

# Select Region of Interest
roi = cv2.selectROI("ROI Selector", image)
# Crop image from x/y position of top left corner of selector to bottom right x/y position
cropped_image = image[int(roi[1]): int(roi[1]) + int(roi[3]), int(roi[0]): int(roi[0]) + int(roi[2])]
crop_resized = cv2.resize(cropped_image, (600, 600))
cv2.imshow("Region of Interest", crop_resized)
cv2.imwrite("processed/cropped_image.jpg", crop_resized)

cv2.waitKey(5000)
cv2.destroyAllWindows()
# print x/y coordinates of starting point and x/y coordinates of the distance from there to the end point
print(roi)