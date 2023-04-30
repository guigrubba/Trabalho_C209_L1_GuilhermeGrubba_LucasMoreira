#Bibliotecas Utilizadas:
import numpy as np
import cv2

img = cv2.imread('imagem.jpeg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #Função que Converte RGB para HSV
img2 = cv2.imread('imagem2.jpeg')
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

minimo = (10, 150, 40)
maximo = (30, 255, 255)

#No modelo HSV temos:
#Vermelho - de 165 a 15
#Verde - de 45 a 75
#Azul - de 90 a 120

#Segmentando a imagem
cv2.imshow('Imagem Inicial', img)
cv2.waitKey(6000)
cv2.destroyAllWindows()

mascara = cv2.inRange(img_hsv, minimo, maximo)
cv2.imshow('Mascara', mascara)
cv2.waitKey(6000)
cv2.destroyAllWindows()
mascaraRGB = cv2.cvtColor(mascara, cv2.COLOR_BGR2RGB) #Convertendo a mascara de HSV para RGB de novo

segmento = cv2.bitwise_and(img, img, mask = mascara)
cv2.imshow('Segmento', segmento)
cv2.waitKey(6000)
cv2.destroyAllWindows()
segmentoRGB = cv2.cvtColor(segmento, cv2.COLOR_BGR2RGB) #Convertendo a mascara de HSV para RGB de novo


#Operações aritméticas

mascaraInvert = cv2.bitwise_not(mascaraRGB)
cv2.imshow('Mascara Invertida', mascaraInvert)
cv2.waitKey(6000)
cv2.destroyAllWindows()

img2_np = np.array(img2)
l, c, p = img2_np.shape

mascaraRGB_np = np.array(mascaraRGB)
r, g, b = mascaraRGB_np.shape

for i in range(l):
    for j in range(c):
        if((mascaraRGB_np[i, j, 0] == 255) & (mascaraRGB_np[i, j, 1] == 255) & (mascaraRGB_np[i, j, 2] == 255)):
            img2_np[i, j, 0] = 1
            img2_np[i, j, 1] = 1
            img2_np[i, j, 2] = 1


cv2.imshow('Imagem Apos recorte', img2_np)
cv2.waitKey(6000)
cv2.destroyAllWindows()

#Blending das imagens:
i = mascaraRGB * segmentoRGB + ((1 - mascaraRGB) * img2_np)
cv2.imshow('Imagem Final', i)
cv2.waitKey(6000)
cv2.destroyAllWindows()
