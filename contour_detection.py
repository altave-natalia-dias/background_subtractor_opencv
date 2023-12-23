import cv2
import numpy as np

# Create background subtractor
fgbg2 = cv2.createBackgroundSubtractorMOG2()

# Open video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, img = cap.read()

    # Apply background subtraction
    fgmask2 = fgbg2.apply(img)

    # Contour Detection
    contours, _ = cv2.findContours(fgmask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # Display the frames
    cv2.imshow('Original', img)
    cv2.imshow('Contour Detection', fgmask2)

    # Check for the 'Esc' key to exit the loop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
