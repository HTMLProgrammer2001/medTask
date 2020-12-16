import cv2
import os


def getCircles(image, circleClassifier):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # find circles
    circles = circleClassifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10)
    )

    return circles

def getImages(path: str) -> list:
	return [
			cv2.imread(os.path.join(path, photo)) for photo in os.listdir(path) if photo.endswith('.jpg') \
					or photo.endswith('.png')
	]

def saveCircles(circlePhoto, prefix='', outDir='./out', centerDir='./outCenter'):
	circleClassifier = cv2.CascadeClassifier('cascade.xml')
	circlePhotoCopy = circlePhoto.copy()
	circlesCoords = getCircles(circlePhoto, circleClassifier)
	
	i = 1

	if not os.path.exists(outDir):
		os.makedirs(outDir)

	for x, y, w, h in circlesCoords:
		# draw rect
		cv2.rectangle(circlePhoto, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# get circle
		circle = circlePhotoCopy[y:y+h, x:x+w]
		
		# save circle
		cv2.imwrite(f"{outDir}/{prefix}_{i}.png", circle)

		# draw center
		cv2.circle(circle, (w//2, h//2), 3, (255, 0, 0), -1)

		# save circle with center
		cv2.imwrite(f"{centerDir}/{prefix}_{i}.png", circle)

		i += 1
