import cv2

import helpers


def main():
	# get paths
	inDir = input('Enter path to directory with data: ')
	outDir = input('Enter path to out directory: ')

	# get all images
	circlePhotos = helpers.getImages(inDir)

	for index, circlePhoto in enumerate(circlePhotos):
		# we get empty photo
		if not circlePhoto.all():
			continue

		# slice and save circles
		helpers.saveCircles(circlePhoto, str(index), outDir)
		# show window with marked circles
		cv2.imshow(str(index), circlePhoto)

	cv2.waitKey()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
