import cv2
import numpy as np

# Create background subtractor
fgbg2 = cv2.createBackgroundSubtractorMOG2()

# Open video capture
cap = cv2.VideoCapture(0)

# Create SimpleBlobDetector parameters
params = cv2.SimpleBlobDetector_Params()
params.filterByCircularity = True
params.minCircularity = 0.8
params.filterByArea = True
params.minArea = 100

detector = cv2.SimpleBlobDetector_create(params)

while True:
    # Read a frame from the camera
    ret, img = cap.read()

    # Apply background subtraction
    fgmask2 = fgbg2.apply(img)

    # Blob Detection
    keypoints = detector.detect(fgmask2)
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the frames
    cv2.imshow('Original', img)
    cv2.imshow('Blob Detection', im_with_keypoints)

    # Check for the 'Esc' key to exit the loop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
