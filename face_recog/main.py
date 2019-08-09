import camera
import faceclassifier
import facedetector

import cv2

if __name__ == '__main__':
    detector = facedetector.FaceDetector()
    image = cv2.imread('test.jpg', 1)
    ret, face = detector.detect(image)
    detector.draw(image)
    cv2.imshow('face', image)
    cv2.waitKey(0)
