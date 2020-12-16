import cv2 as cv
import numpy as np
import imutils
import math

import helpers


colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (100, 100, 100), (0, 0, 0), (255, 255, 255), (255, 0 ,0)]

def getImageDistances(img, name):
	print('')

	# find center
	centerX = img.shape[0] // 2
	centerY = img.shape[1] // 2

	cloneImg = img.copy()

	# divide circle on the 12 sections
	for i, angle in enumerate(np.arange(0, 2 * math.pi, math.pi / 6)):
		distances = []

		# rotate image to current angle
		cloneImg = imutils.rotate(img, angle = (i - 3) * 30)

		# draw center
		cv.circle(cloneImg, (centerX, centerY), 2, (255, 0, 0), 2)

		distances = []

		# use 2 grad as one step
		for a in np.arange(0, math.pi / 6, math.pi / 90):
			# was red line or not
			innerPoint = None
			wasEnd = True

			# get line equalation
			endX = centerX + int(math.cos(a) * cloneImg.shape[0])
			endY = centerY + int(math.sin(a) * cloneImg.shape[1])
			eq = helpers.getEq((centerX, centerY), (endX, endY))

			endX = min(endX, cloneImg.shape[0] - 1)
			endX = max(endX, 0)			

			# get range
			maxX = max(centerX, endX)
			minX = min(centerX, endX)

			for x in range(minX, maxX):
				y = int(eq(x))

				if y >= cloneImg.shape[1]:
					continue

				# get cell value
				cell = cloneImg[y, x]

				# it's black point
				if helpers.isBlack(cell) and not innerPoint:
					innerPoint = [x, y]
				elif not helpers.isBlack(cell) and innerPoint:
					# it's out point
					outPoint = [x, y]

					# get distance
					d = helpers.getDistance(innerPoint, outPoint)

					# too tiny
					if d < 3:
						continue

					# add distance
					distances.append(d)

					# draw line
					cv.line(cloneImg, (innerPoint[0], innerPoint[1]), (outPoint[0], outPoint[1]), colors[i], 1)
					break

			else:
				wasEnd = False

			if not wasEnd and innerPoint:
				outPoint = [cloneImg.shape[0] - 1, int(eq(cloneImg.shape[0] - 1))]

				# get distance
				d = helpers.getDistance(innerPoint, outPoint)

				# too tiny
				if d < 3:
					continue

				# add distance
				distances.append(d)

				# draw line
				cv.line(cloneImg, (innerPoint[0], innerPoint[1]), (outPoint[0], outPoint[1]), colors[i], 1)


		cv.imshow(str(f"{name}_{i}"), cloneImg)
		print(f"Distance for {name} section {i+1} = {np.average(distances)}")

	print('')
