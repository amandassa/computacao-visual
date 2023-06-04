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