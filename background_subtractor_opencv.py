import numpy as np
import cv2

# Create background subtractors
fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG()

# Open video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, img = cap.read()

    # Apply background subtraction
    fgmask1 = fgbg1.apply(img)
    fgmask2 = fgbg2.apply(img)
    fgmask3 = fgbg3.apply(img)

    # Display the frames
    cv2.imshow('Original', img)
    cv2.imshow('MOG', fgmask1)
    cv2.imshow('MOG2', fgmask2)
    cv2.imshow('GMG', fgmask3)

    # Check for the 'Esc' key to exit the loop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
