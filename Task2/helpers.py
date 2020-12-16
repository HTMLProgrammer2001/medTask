import os
import cv2


def getImages(path: str) -> dict:
	return {
			photo: cv2.imread(os.path.join(path, photo)) for photo in \
				os.listdir(path) if photo.endswith('.jpg') or photo.endswith('.png')
	}
