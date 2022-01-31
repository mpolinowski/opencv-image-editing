import cv2

image = cv2.imread('resources/test-image.jpg')

# Splitting the image into color channels
b, g, r = cv2.split(image)

cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.imwrite("processed/red_channel.jpg", r)

# Re-join all colour channels
image_color_channels = cv2.merge((b, g, r))
cv2.imshow("Image Colour Channels", image_color_channels)

# Change colour space
image_luv = cv2.cvtColor(image, cv2.COLOR_RGB2LUV)
cv2.imshow("LUV Colour Space", image_luv)

cv2.waitKey(5000)
cv2.destroyAllWindows()