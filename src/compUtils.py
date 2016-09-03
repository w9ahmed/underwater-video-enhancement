import cv2
import time

def h_264():
	return cv2.CV_FOURCC('H','2','6','4')

def splitVideo():
	# Step 1: Check if video size is getting larger than 32GBs

	# Step 2: If Step 1, then stop and start recording a new video