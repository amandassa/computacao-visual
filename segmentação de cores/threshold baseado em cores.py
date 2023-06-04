import cv2
from cv2 import imread
import numpy as np
from pathlib import Path

'''
Atividade em dupla: Amanda Silva, Antony Araújo
'''

def segment_image(image, lower_range, upper_range):
    # Converter a imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Criar uma máscara usando os intervalos de cores fornecidos
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # Aplicar o processamento morfológico para remover ruídos
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Retornar a imagem binária resultante
    return mask

# Carregar a imagem
image_path = Path('/home/amandassa/Repositorios/OpenCV/computacao-visual/segmentação de cores/pecas_lego.jpg')
image = imread(str(image_path))

# Definir os intervalos de cores para cada cor predominante
lower_green = np.array([35, 50, 50])  # Verde
upper_green = np.array([80, 255, 255])
lower_red = np.array([0, 50, 50])  # Vermelho
upper_red = np.array([10, 255, 255])
lower_blue = np.array([100, 50, 50])  # Azul
upper_blue = np.array([130, 255, 255])

# Segmentar a imagem para cada cor predominante
green_mask = segment_image(image, lower_green, upper_green)
red_mask = segment_image(image, lower_red, upper_red)
blue_mask = segment_image(image, lower_blue, upper_blue)

# Exibir as imagens binarizadas resultantes
cv2.imshow("Green Mask", green_mask)
cv2.imshow("Red Mask", red_mask)
cv2.imshow("Blue Mask", blue_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
