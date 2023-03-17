import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem))
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem original', image)

# Imagem original para negativo
negativo = ~image

cv2.namedWindow('Imagem filtro negativo', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem filtro negativo', negativo)

# Imagem negativo para normal com negativo
imagem2 = ~negativo

cv2.namedWindow('Imagem filtro negativo', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem filtro negativo', negativo)

# Imagem negativo para P&B
imagemcinza = cv2.cvtColor(negativo, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem negativo em tons de cinza', imagemcinza)

cv2.waitKey(0)
cv2.destroyAllWindows()