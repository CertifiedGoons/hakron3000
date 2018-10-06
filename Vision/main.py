import cv2
import numpy as np
import urllib.request

#img = cv2.imread('card.jpeg')
url = 'http://camera.accidentallycoded.com/shot.jpg'

vidFeed = urllib.request.urlopen(url)
vidNp = np.array(bytearray(vidFeed.read()),dtype=np.uint8)
vid = cv2.imdecode(vidNp, -1)

#cv2.namedWindow("Card", flags=cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow("Card", vid)

cv2.waitKey(0)
