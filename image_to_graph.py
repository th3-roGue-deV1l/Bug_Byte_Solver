import cv2 as cv
import numpy as np

image_path = 'puzzle.png'

image = cv.imread(image_path)



# So this converted the image into the path nodes only, so that might be helpful
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
lower_green = np.array([35,40,40])
upper_green = np.array([70,255,255])
lower_blue = np.array([100,40,40])
upper_blue = np.array([130,255,255])
lower_white = np.array([100,40,40])
upper_white = np.array([180,255,255])
mask1 = cv.inRange(hsv, lower_green, upper_green)
mask2 = cv.inRange(hsv, lower_blue, upper_blue)
mask3 = cv.inRange(hsv, lower_white, upper_white)
mask = cv.bitwise_or(mask1, mask2)
mask = cv.bitwise_or(mask, mask3)
result = cv.bitwise_and(image, image, mask=mask)

cv.imshow('result', result)

cv.waitKey(0)
cv.destroyAllWindows()
