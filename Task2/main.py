import cv2
import numpy as np

import helpers


if __name__ == '__main__':
    photos = helpers.getImages('./input')

    for name, img in photos.items():
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # меняем цветовую модель с BGR на HSV 
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        canny = cv2.Canny(thresh, 0, 0)

        contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        # fill inner
        # for i in range(len(contours)):
        #     cv2.drawContours(img, contours, i, (0, 255, 0), -1)

        # draw contours
        for i in range(len(contours)):
            cv2.drawContours(img, contours, i, (0, 0, 255))

        cv2.imshow(str(name), img)

        cv2.imwrite(f"./out/{name}", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
