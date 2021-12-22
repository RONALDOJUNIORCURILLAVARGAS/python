import cv2

img = cv2.imread('ruido.jpg',1)
img_redimensionada= cv2.resize(img,(400,400))
#Filtro BLUR
blur= cv2.blur(img_redimensionada,(4,4))
#Filtro PyrDown
pyrdwn=cv2.pyrDown(img_redimensionada)
#Filtro Pyrup
pyrup=cv2.pyrUp(img_redimensionada)
#Filtro Gaussiano (Desviacion estandar)
gauss= cv2.GaussianBlur(img_redimensionada,(5,5),5,5)
#Filtrops 
pyrMS=cv2.pyrMeanShiftFiltering(img_redimensionada,70,71)

#visualiizacion de los resultados en los filtros
cv2.imshow('original',img_redimensionada)
cv2.imshow('blur',blur)
cv2.imshow('PyrDown',pyrdwn)
cv2.imshow('PyrUp',pyrup)
cv2.imshow('Gauss',gauss)
cv2.imshow('pyrms',pyrMS)
#
cv2.waitKey(0)
cv2.destroyAllWindows()