import cv2
import numpy as np

intensidade = \
    [[255,0,0,255,255,255,255,255],[0,0,0,0,255,255,255,255],[255,0,0,0,255,255,255,255],[255,0,0,255,255,255,255,255],[255,255,0,0,255,0,0,255],[255,255,255,0,0,0,0,0],[255,255,255,255,0,0,0,0],[255,255,255,255,255,0,0,0]]


imagem = np.array(intensidade, dtype=np.uint8)


elem1 = cv2.getStructuringElement( cv2.MORPH_CROSS, ( 3, 3 ) ) # Elemento estruturante
elem2 = cv2.getStructuringElement( cv2.MORPH_RECT, ( 3, 3 ) ) # Elemento estruturante

erosao = cv2.morphologyEx(~imagem,cv2.MORPH_ERODE,elem1)

cv2.imshow('Imagem original',imagem)
cv2.imshow('Imagem Erosão',erosao)

cv2.waitKey(0)