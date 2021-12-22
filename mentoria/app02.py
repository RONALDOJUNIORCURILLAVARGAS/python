import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('ruido.jpg')

#cv2.imshow('original',img)
#convertimos a escala de grises a la imagen
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Aplicacion de suavizado gaussiano en la imagen
gauss=cv2.GaussianBlur(img,(5,5),0)

#Convertimos la imagen de BGR a RGB
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Filtros de convolucion de 2 dimensiones


#Generamos un kernel utilizando con la funcion ones,estamos generando una matriz de 3x3 con valores flotantes
#y lo dividimos entre 9 para obtener el promedio
kernel = np.ones((3,3),np.float32)/9

f1=cv2.filter2D(img, -1,kernel)
f2 = cv2.blur(img,(3,3))
f3=cv2.GaussianBlur(img,(3,3),0)
f4=cv2.medianBlur(img,3)
f5=canny=cv2.Canny(gauss,50,150)

#creamos un arreglo de los resultados de los filtros de las figuras
f=[f1,f2,f3,f4,gauss,f5]
#creamos un arreglo de los titulos de los filtros de las figuras
t=['FILTRO 2D','FILTRO BLUR','FILTRO GAUSSIANO','FILTRO MEDIANA','GAUSS','FILTRO CANNY']
#Creamos un ciclo for utilizando la variable i y el rango de 6 ciclos
for i in range(6):
    #Generamos nuestro arreglo de figuras(72 filas y 3 columnas) utilizamos la variable i
    #para recorrer cada uno de las posiciones
    plt.subplot(2,3,i+1)
    #Mostramos cada uno de las imagenes de los resultado de cada uno de las posiciones
    #con un valor minimo de 0 y maximo de 255
    plt.imshow(f[i],vmin=0,vmax=255)
    #Mostramos cada uno de los titulos con sus posiciones correspondientes
    #Recorremos el contenido de la variable t en mi ciclo for
    plt.title(t[i])
    #Evitamos que se mueste la enumeracion y los ejes de nuestras figuras
    plt.xticks([]),plt.yticks([])
#mostramos nuestro arreglo de figuras
plt.show()
  
cv2.imshow('escala',gris)

cv2.waitKey(0)
cv2.destroyAllWindows()
