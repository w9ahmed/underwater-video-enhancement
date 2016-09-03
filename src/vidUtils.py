import cv2
import datetime
import os
import dirUtils

def addTextOnVideo(image, text, x, y):
	""" Add text on the video """
	cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255,255, 255), thickness=1, lineType=cv2.CV_AA)

def configureVideos(fileName = None):
	fourcc = cv2.cv.CV_FOURCC('X','V','I','D')

	videoFileName = str(datetime.datetime.now());
	dirUtils.createOutputDirectory()

	if fileName != None:
		videoFileName = videoFileName + "_" + fileName

	return videoFileName, cv2.VideoWriter(videoFileName + ".avi", fourcc, 20.0, (640,480))