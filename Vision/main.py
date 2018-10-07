import cv2
import numpy as np

URL = "http://192.168.1.7:8080/video"
BLUR_AMOUNT = (5, 5)
CAM = cv2.VideoCapture(URL)

while True:
    ret, frame = CAM.read()
    if ret:
        dupFrame = cv2.copyMakeBorder(frame, 0, 0, 0, 0, cv2.BORDER_REPLICATE)

        # Manipulate frame
        bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.blur(bw, BLUR_AMOUNT, 1000)
        ret, thresh = cv2.threshold(blurred, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea,reverse=True)

        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, .02 * perimeter, True)

            # Draw boxes in separate window
            box = np.int0(approx)
            cv2.drawContours(dupFrame, [box], 0, (255, 0, 0), 2)

            # Affine Transform
            h = np.array([[0, 0], [449, 0], [449, 449], [0, 449]], np.float32)  
            transform = cv2.getPerspectiveTransform(approx, h)
            # warp = cv2.warpPerspective(frame, transform, (450, 450))

        cv2.imshow("Boxes", dupFrame)

            # print(type(rect))


        # Display frame to window
        image = frame
        cv2.imshow("IP Camera", image)

        # Close on escape
        if cv2.waitKey(1) == 27:
            exit(0)