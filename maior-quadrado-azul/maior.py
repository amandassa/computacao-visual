# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import cv2
import numpy as np
from pathlib import Path

''' atividade em dupla - Antony, Amanda '''

caminhoImagem = Path('computacao-visual/maior-quadrado-azul')

src = cv2.imread(str(caminhoImagem / "figuras.jpg"))
blurred = cv2.GaussianBlur(src, (5, 5), 0)

resized = imutils.resize(src, width=300)
ratio = src.shape[0] / float(resized.shape[0])

image_in_HSV = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
cross_element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3)) # Elemento estruturante

# lower_blue = np.array([62, 0, 5])  # Azul
# upper_blue = np.array([136, 255, 255])

lower_blue = np.array([65, 40, 230])  # Azul
upper_blue = np.array([90, 80, 255])

blue_mask = cv2.inRange(image_in_HSV, lower_blue, upper_blue)
open_operation = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, cross_element) #threshold azul
result_blue_mask = cv2.bitwise_and(src, src, mask=open_operation)

# maior contorno

contours = cv2.findContours(open_operation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

sd = ShapeDetector()

for c in contours:
    # compute the center of the contour, then detect the name of the
	# shape using only the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    shape = sd.detect(c)

    cv2.drawContours(src, [c], -1, (0, 0, 255), 6)
    cv2.putText(
        src, 
        "Quadrado Azul", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

cv2.namedWindow('Azul', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Azul', result_blue_mask)
cv2.namedWindow('Maior quadrado azul', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Maior quadrado azul', src)
cv2.waitKey(0)
