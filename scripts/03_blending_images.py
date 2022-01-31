import cv2

background = cv2.imread('resources/test-image.jpg')
foreground = cv2.imread('processed/red_channel.jpg')

blurred_background = cv2.GaussianBlur(background, (1,1), 0)

blended_image = cv2.addWeighted(blurred_background, 0.2, foreground, 0.8, 0.0)
cv2.imshow("Blended Image", blended_image)

cv2.waitKey(5000)
cv2.destroyAllWindows()