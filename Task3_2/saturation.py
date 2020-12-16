import cv2 as cv
import numpy as np
import imutils
import math

import helpers


colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (100, 100, 100), (0, 0, 0), (255, 255, 255), (255, 0 ,0)]

def getImageSaturation(img, name):
	# find center
	centerX = img.shape[0] // 2
	centerY = img.shape[1] // 2

	# points arrays
	blackPoints = []
	sectionPoints = [[] for i in range(12)]

	# get hsv image
	hsvImage = cv.cvtColor(img, cv.COLOR_BGR2HSV)

	for y in range(0, img.shape[0]):
		for x in range(0, img.shape[1]):

			# this point is black
			if helpers.isBlack(img[y, x]):
				# get saturation
				sat = hsvImage[y, x][1]

				# add point to list
				blackPoints.append({'x': x, 'y': y, 'sat': sat})

	for point in blackPoints:
		# calculate angle of point
		angle = math.atan2(point['y'] - centerY, point['x'] - centerX)
		angle += math.pi / 2

		# get index
		index = math.floor(angle / (math.pi / 6))

		if index == 12:
			index = 11

		# add saturation to section array
		sectionPoints[index].append(point['sat'])
		img[point['y'], point['x']] = colors[index]

	
	for i, section in enumerate(sectionPoints):
		section = np.array([el for el in section if el != 0])

		# calculate koef
		avg = np.min(section)
		maxS = np.max(section)

		print(f"Saturation koef for section {i + 1} is {avg/maxS}")

	cv.imshow(name, img)
