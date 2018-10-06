import cv2
import numpy as np

img = cv2.imread('card.jpeg')

cv2.namedWindow("Card", flags=cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow("Card", img)

cv2.waitKey(0)
