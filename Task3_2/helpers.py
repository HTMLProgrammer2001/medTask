import os
import cv2
from math import sqrt
import numpy as np


def getImages(path: str) -> dict:
	return {
			photo: cv2.imread(os.path.join(path, photo)) for photo in \
				os.listdir(path) if photo.endswith('.jpg') or photo.endswith('.png')
	}


def getEq(point1, point2):
	return lambda x: (x - point2[0]) * (point2[1] - point1[1]) / (point2[0] - point1[0]) + point2[1]


def getDistance(point1, point2):
	return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def isBlack(cell) -> bool:
	return cell[0] <= 150 and cell[1] <= 150 and cell[2] <= 150
