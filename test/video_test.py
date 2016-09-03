import numpy as np
import cv2
import filterUtils
import sys

videos = ["vid1.mp4", "vid2.avi", "vid3.mp4"]
video = videos[1]
if len(sys.argv) > 1:
	index = int(sys.argv[1])
	if index > 2:
		index = 1
	video = videos[index]

cap = cv2.VideoCapture(video)

while(cap.isOpened()):
    ret, frame = cap.read()

    processed = filterUtils.clearImage(frame)

    cv2.imshow('original',frame)
    cv2.imshow('processed',processed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()