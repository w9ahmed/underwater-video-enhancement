import numpy as np
import cv2

def clearImage(image):
	# Convert the image from BGR to gray
	dark_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	channels = cv2.split(image)

	# Get the maximum value of each channel
	# and get the dark channel of each image
	# record the maximum value of each channel
	a_max_dst = [ float("-inf") ]*len(channels)
	for idx in xrange(len(channels)):
		a_max_dst[idx] = channels[idx].max()

	dark_image = cv2.min(channels[0],cv2.min(channels[1],channels[2]))

	# Gaussian filtering the dark channel
	dark_image = cv2.GaussianBlur(dark_image,(25,25),0)

	image_t = (255.-0.95*dark_image)/255.
	image_t = cv2.max(image_t,0.5)

	# Calculate t(x) and get the clear image
	for idx in xrange(len(channels)):
		# channels[idx] = cv2.max(cv2.add(cv2.subtract(channels[idx].astype(np.float32),int(a_max_dst[idx]))/image_t,int(a_max_dst[idx])),0.0)
		channels[idx] = cv2.max(cv2.add(cv2.subtract(channels[idx].astype(np.float32),int(a_max_dst[idx]))/image_t,int(a_max_dst[idx])),0.0)/int(a_max_dst[idx])*255
		channels[idx] = channels[idx].astype(np.uint8)

	return cv2.merge(channels)

def enhanceImage(image):
	# Step 1: Histogram Stretching (Normalization)

	# Step 2: Convert RGB image to HSV
	image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

	# Step 3: Apply Histogram Stretching to S and V channels
	h,s,v = cv2.split(image)
	
	maxValue, minValue = s.max(), s.min()

	# Then to stretch is a simple math
	s = 255.0*(s-minValue) / (maxValue - minValue)
	maxValue, minValue = v.max(), v.min()
	v = 255.0*(v-minValue) / (maxValue - minValue)
	# maxValue, minValue = h.max(), h.min()
	h = 255.0*(h-minValue) / (maxValue - minValue)

	image = cv2.merge((h, s, v))

	# Step 4: Convert back to RGB
	image = image.astype(np.uint8)
	image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
	return image