import cv2 as cv
import numpy as np

caminhoImagem = '/home/amandassa/Repositorios/OpenCV/computacao-visual/threshold-adaptativo/Ground_Truth/'
def fillHoles(src):
    contours,hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    dst = np.zeros(src.shape, np.uint8)
    color = 255
    for i in range(len(contours)):
        cv.drawContours(dst, contours,i, color, -1, 8, hierarchy, 0)
    return dst

def main():
    for i in range(7):
        variavel = 'Imagem 0'+str(i+1)
        print(variavel)    
        strImagem = 'Imagem'
        strGround = 'Ground Truth'
        strResult = 'Resultado Threshold'
        cv.namedWindow(strImagem, cv.WINDOW_GUI_EXPANDED)
        cv.namedWindow(strGround, cv.WINDOW_GUI_EXPANDED)
        cv.namedWindow(strResult, cv.WINDOW_GUI_EXPANDED)
        caminhoIn = '0'+str(i+1)+'.jpg'
        caminhoOut = 'gt/gt0'+str(i+1)+'.png' 
        npImagem = cv.imread(caminhoImagem + caminhoIn,cv.IMREAD_GRAYSCALE)
        if (npImagem is None): print('Erro na abertura da imagem!'); return
        npGround = cv.imread(caminhoImagem + caminhoOut,cv.IMREAD_GRAYSCALE)
        if (npImagem is None): print('Erro na abertura do ground truth!'); return
        cv.imshow(strImagem, npImagem)
        cv.imshow(strGround, npGround)

        npNorm = cv.normalize(npImagem,None,0, 255, cv.NORM_MINMAX)
        npSuavizacao = cv.GaussianBlur(npNorm, (7,7),0,0) ## suavização mantida pois remove a maior parte do ruído na parte inferior
        passabaixa = cv.blur(npSuavizacao,(3,3))      ### ADICIONADO: PASSA BAIXA remove ruído que a suavização não atingiu na parte inferior da imagem
        npThreshold = cv.adaptiveThreshold(passabaixa,  255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 15, 3)
        npMorfologia = cv.morphologyEx(npThreshold,cv.MORPH_CLOSE, cv.getStructuringElement( cv.MORPH_ELLIPSE, ( 11, 11 ) ))

        image_result = fillHoles(npMorfologia)

        cv.imshow(strResult, image_result)

        #Verdadeiro Positivo
        image_vp = cv.bitwise_and(npGround,image_result)
        #Verdadeiro Negativo
        image_vn = cv.bitwise_and(~npGround,~image_result)
        #Falso Positivo
        image_fp = cv.bitwise_and(~npGround,image_result)
        #Falso Negativo
        image_fn = cv.bitwise_and(npGround,~image_result)

        taxa_vp = cv.countNonZero(image_vp)/cv.countNonZero(npGround)*100
        taxa_vn = cv.countNonZero(image_vn)/cv.countNonZero(~npGround)*100
        taxa_fp = cv.countNonZero(image_fp)/cv.countNonZero(~npGround)*100
        taxa_fn = cv.countNonZero(image_fn)/cv.countNonZero(npGround)*100

        
        print("Verdadeiro Positivo: {:.2f} %".format(taxa_vp)) 
        print("Verdadeiro Negativo: {:.2f} %".format(taxa_vn))
        print("Falso Positivo: {:.2f} %".format(taxa_fp))
        print("Falso Negativo: {:.2f} %".format(taxa_fn))
        print("----------------------------" )

        cv.waitKey(0)
cv.destroyAllWindows()

if __name__ == '__main__':
    main()