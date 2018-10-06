import cv2
import numpy as np
import urllib.request

img = cv2.imread('card.jpeg')
url = 'http://192.168.1.7:8080/video'

vidFeed = urllib.request.urlopen(url)
vidNp = np.array(bytearray(vidFeed.read()), dtpye = np.uint8)
vid = cv2.imdecode(vidNp, -1)
cv2.imshow('test', vid)

cv2.namedWindow("Card", flags=cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow("Card", img)

cv2.waitKey(0)
