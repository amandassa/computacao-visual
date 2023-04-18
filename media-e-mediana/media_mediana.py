import cv2
import glob
import numpy as np

# Abre as imagens de um diretório e armazena em um vetor
filelist = glob.glob('imagens\\*.png')
for file in filelist:
    print(file)
imagens_stack = np.array([np.array(cv2.imread(fname,0)) for fname in filelist])

# Armazena as colunas e linhas de uma imagem
rows,cols = imagens_stack[0].shape
imagem_count = len(imagens_stack)

# Cria uma imagem vazia para armazenar o resultado
resultadoMediana = np.zeros((rows,cols),np.uint8)
resultadoMedia = np.zeros((rows,cols),np.uint8)
...
# Varre as linhas e colunas da imagem
for r in range(rows):
    for c in range(cols):
        # Ordena em um vetor o mesmo pixel de todas imagens
        xyTodasImagemsMediana = np.sort(imagens_stack[:,r,c])
        # Falta pegar o valor do meio do vetor e atribuir ao pixel do resultado (Mediana)
        resultadoMediana[r][c] = xyTodasImagemsMediana[49]
        # Armazena em um vetor o mesmo pixel de todas imagens
        xyTodasImagemsMedia = np.sort(imagens_stack[:,r,c])
        # Falta somar o vetor e dividir pela quantidade de imagens (Média)
        resultadoMedia[r][c] = round(sum(imagens_stack[:,r,c]))/imagem_count
        
cv2.imshow('Mediana da Imagem', resultadoMediana)
cv2.imshow('Média da Imagem', resultadoMedia)

cv2.imwrite('result/median_image.png', resultadoMediana)
cv2.imwrite('result/mean_image.png', resultadoMedia)

cv2.waitKey(0)
cv2.destroyAllWindows()
