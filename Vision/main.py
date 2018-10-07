import cv2
import urllib 
import numpy as np

stream = urllib.urlopen('http://camera.accidentallycoded.com/video')
bytes = ''

def displayFrame(frame):
    cv2.imshow("IP Camera", frame)

while True:

    # Get frame from video feed
    bytes += stream.read(16384)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        
        # Manipulate frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display frame to window
        displayFrame(gray_frame)

        # Close on escape
        if cv2.waitKey(1) == 27:
            exit(0)