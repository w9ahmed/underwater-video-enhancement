import os
import datetime

def createOutputDirectory():
	checkOrCreateDirectory("output")

	videoCurrentFolderName = str(datetime.datetime.now().date())

	checkOrCreateDirectory("output/" + videoCurrentFolderName + "/original")
	checkOrCreateDirectory("output/" + videoCurrentFolderName + "/processed")


def checkOrCreateDirectory(folderName):
	""" Checks if a folder exists or not, 
		if it exist, do nothing
		else create the folder """
	if not os.path.exists(folderName):
	    os.makedirs(folderName)

def moveVideoToItsDirectory(fileName, processed = False):
	currentDate = str(datetime.datetime.now().date())
	currentDirectory = os.path.dirname(os.path.realpath(fileName));

	outputDirectory = "/output/" + currentDate

	if processed:
		outputDirectory = outputDirectory + "/processed/"
	else:
		outputDirectory = outputDirectory + "/original/"

	os.rename(currentDirectory + "/" + fileName, currentDirectory + outputDirectory + fileName)

def checkFileSize(file, size):
	currentSize = os.stat(file + ".avi").st_size
	if((currentSize*1.0)/(1024*1024*1024) > size):
		return True
	return False