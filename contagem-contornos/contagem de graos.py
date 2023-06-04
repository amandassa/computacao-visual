import cv2
from pathlib import Path

''' Dupla rodrigo, amanda '''

caminhoImagem = Path('computacao-visual/contagem-contornos')

imagem = cv2.imread(str(caminhoImagem / "arroz.jpg"))

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(imagem_cinza, (9, 9), 0)

cv2.namedWindow("imagem cinza", cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("imagem cinza", blurred)

imagem_binaria = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, -3)

elem1 = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, ( 17, 17 ) ) # Elemento estruturante

abertura1 = cv2.morphologyEx(imagem_binaria,cv2.MORPH_OPEN ,elem1)

contornos, _ = cv2.findContours(abertura1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

num_graos = len(contornos)

cv2.drawContours(imagem, contornos, -1, (255, 255, 255), -1)

cv2.putText(imagem, f'Numero de graos: {num_graos}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.namedWindow("imagem processada", cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("imagem processada", abertura1)
cv2.namedWindow("Contagem de Graos de Arroz", cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Contagem de Graos de Arroz', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()