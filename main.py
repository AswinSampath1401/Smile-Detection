import cv2
import os

sample_image =cv2.imread('E:\\Smile Detection\\Smile-Detection\\Images\\smile\\msd.jpg')

cv2.imshow('Smile',sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()