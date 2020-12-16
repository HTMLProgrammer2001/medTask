import cv2 as cv
import numpy as np
import math
import imutils

import helpers
from distance import getImageDistances
from saturation import getImageSaturation


def main():
	photos = helpers.getImages('./in')

	for name, img in photos.items():
		# calculate image kron distances
		getImageDistances(img, name)

		# calculate image saturation koef
		getImageSaturation(img, name)

	cv.waitKey(0)
	cv.destroyAllWindows()



if __name__ == '__main__':
	main()
