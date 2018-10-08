import cv2
import numpy as np

#url to video stream (Can be device location)
URL = "http://192.168.1.7:8080/video"
#global blur amount
BLUR_AMOUNT = (5, 5)
#capturing vudeo feed from url
CAM = cv2.VideoCapture(URL)

while True:
    #get frame from, and test ret from video feed
    ret, frame = CAM.read()
    if ret:
        dupFrame = cv2.copyMakeBorder(frame, 0, 0, 0, 0, cv2.BORDER_REPLICATE)

        # Manipulate frame
        #convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #blur the image to reduce noise
        blurred = cv2.blur(gray, BLUR_AMOUNT, 1000)
        #use Otsu's thresholding to find best threshold value (from https://is.gd/WChzc5)
        ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #form contours based on threshold, contour retrieval mode, and the contour approximation method
        contours, hierarchy, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #sort contours by size
        contours = sorted(contours, key=cv2.contourArea,reverse=True)

        #form single contours from array of contours
        for contour in contours:
            
            #approximating contours for transforming (dunno if we're going to end up using this)
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, .02 * perimeter, True)

            #minAreRect used for drawing rectangle contours around rotated cards
            rect = cv2.minAreaRect(contour)
            #get four corners from minAreaRect in order to drawContours
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            #draw contours!
            cv2.drawContours(dupFrame,[box],0,(0,0,255),2)
            
            # Affine Transform
            #h = np.array([[0, 0], [449, 0], [449, 449], [0, 449]], np.float32)  
            # transform = cv2.getPerspectiveTransform(approx, h)
            # warp = cv2.warpPerspective(frame, transform, (450, 450))

        cv2.imshow("Boxes", dupFrame)

            # print(type(rect))


        # Display frame to window
        image = frame
        cv2.imshow("IP Camera", image)

        # Close on escape
        if cv2.waitKey(1) == 27:
            exit(0)