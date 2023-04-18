'''
import glob
import cv2
from pathlib import Path


def read_img(img_list, img):
    n = cv2.imread(img, 0)
    img_list.append(n)
    return img_list

path = glob.glob("Ground_Truth/*.jpg") #or jpg
list_ = []

cv_image = [read_img(list_, img) for img in path]

for image in cv_image:
    cv2.namedWindow("Imagem original")
    cv2.imshow("Imagem original", image)

    thresholdnormal = cv2.threshold(image, 25, 255, cv2.THRESH_BINARY)
    cv2.namedWindow("Threshold Normal")
    cv2.imshow("Imagem original", thresholdnormal)

    thresholdadap = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, -3)
    cv2.namedWindow('Resultado threshold adaptativo')
    cv2.imshow('Resultado threshold adaptativo', thresholdadap)
'''

import cv2
import os

def adaptive_threshold_all_images(directory_path):
    for filename in os.listdir(directory_path):
        # Ler a imagem
        img_path = os.path.join(directory_path, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        # Aplicar o threshold adaptativo
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 45, -3)
        
        # Exibir o resultado
        cv2.namedWindow('Imagem original '+filename)
        cv2.imshow('Imagem original '+filename, img)
        cv2.namedWindow('Threshold adaptativo '+filename)
        cv2.imshow('Threshold adaptativo '+filename, thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

adaptive_threshold_all_images("Ground_Truth")