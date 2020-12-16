import cv2 as cv
import math
import numpy as np

import helpers


colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (100, 100, 100), (0, 0, 0), (255, 255, 255), (255, 0 ,0)]

def main():
	photos = helpers.getImages('./in')

	for name, img in photos.items():
		# find center
		centerX = img.shape[0] // 2
		centerY = img.shape[1] // 2

		cloneImg = img.copy()

		outContours = []
		innerCountours = []

		cv.circle(cloneImg, (centerX, centerY), 2, (255, 0, 0), 2)

		for i, angle in enumerate(np.arange(0, 2 * math.pi, math.pi / 6)):
			eY = centerY + int(math.sin(angle) * img.shape[1] // 2)
			eX = centerX + int(math.cos(angle) * img.shape[0] // 2)

			#cv.line(img, (centerX, centerY), (x, y), (0, 255, 255), 1)

			distances = []
			for a in np.arange(angle, angle + math.pi / 6, math.pi / 180):
				innerPoint = None

				endX = centerX + int(math.cos(a) * img.shape[0])
				endY = centerY + int(math.sin(a) * img.shape[1])
				eq = helpers.getEq((centerX, centerY), (endX, endY))

				endX = min(endX, img.shape[0] - 1)
				endX = max(endX, 0)			

				maxX = max(centerX, endX)
				minX = min(centerX, endX)

				for x in range(minX, maxX):
					y = int(eq(x))

					if y < 0 or y >= img.shape[1]:
						continue

					cell = img[y, x]

					if cell[0] == 0 and cell[1] == 0 and cell[2] == 255:
						if not innerPoint:
							innerPoint = [x, y]
						else:
							outPoint = [x, y]
							d = helpers.getDistance(innerPoint, outPoint)

							distances.append(d)
							cv.line(cloneImg, (innerPoint[0], innerPoint[1]), (x, y), colors[i], 1)
							break

			avgDistance = np.average(distances)
			print(f"Distance for {name} section {i+1} = {avgDistance}")

			#cv.line(img, (centerX, centerY), (eX, eY), (0, 255, 255), 1)

		cv.imshow(str(name), cloneImg)

	cv.waitKey(0)
	cv.destroyAllWindows()


if __name__ == '__main__':
	main()
