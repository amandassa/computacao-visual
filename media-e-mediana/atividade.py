import cv2
import glob
import numpy as np

# Abre as imagens de um diretório e armazena em um vetor
filelist = glob.glob("./Satelite_ruido/*.png")
imagens_stack = np.array([np.array(cv2.imread(fname,0)) for fname in filelist])

# Armazena as colunas e linhas de uma imagem
rows,cols = imagens[0].shape
# Cria uma imagem vazia para armazenar o resultado
resultadoMediana = np.zeros((rows,cols),np.uint8)
resultadoMedia = np.zeros((rows,cols),np.uint8)

# Varre as linhas e colunas da imagem
for r in range(rows):
for c in range(cols):

# Ordena em um vetor o mesmo pixel de todas imagens
xyTodasImagemsMediana = np.sort(imagens[:,r,c])
# Falta pegar o valor do meio do vetor e atribuir ao pixel do resultado (Mediana)

# Armazena em um vetor o mesmo pixel de todas imagens
xyTodasImagemsMedia = imagens[:,r,c]
# Falta somar o vetor e dividir pela quantidade de imagens (Média)