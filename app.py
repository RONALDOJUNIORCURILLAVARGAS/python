
#-----------------Importamos las librerias
from types import FrameType
from comtypes.hresult import DISP_E_DIVBYZERO
import cv2
import SeguimientoManos as sm
import numpy as np
import os
#-----------Librerias para controlar el volumen
from  ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#parametros para OS
#DIRECCION DEL ARCHIVO DONDE SE ENCUENTRA LAS FOTOS
dataPath = 'C:/Users/ronaldo/Desktop/Reconocimiento_facial/data'
imagePaths = os.listdir(dataPath)
print('imagePaths =',imagePaths)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#ruta del archivo xml
face_recognizer.read('./asistente_IA/modeloLBPHFace.xml')
#-----------Parametros de la camara
anchoCam, altoCam = 640, 480

#--------Lectura de la camara
#-- PARA CAPTURA DE VIDEO EN VIVO
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#-- PARA UTILIZAR UN VIDEO
#cap = cv2.VideoCapture('./asistente_IA/astudillo.mp4')
cap.set(3,anchoCam)
cap.set(4,altoCam)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


#---------Creamos el objeto que almacenara nuestra clase
detector = sm.detectormanos(maxManos=1,Confdeteccion=0.7)

#------Control de Audio del PC
dispositivos = AudioUtilities.GetSpeakers()
interfaz = dispositivos.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volumen = cast(interfaz, POINTER(IAudioEndpointVolume))
RangoVol= volumen.GetVolumeRange()
#print(RandoVol)
VolMin = RangoVol[0]
VolMax = RangoVol[1]

while True:
    ret, frame = cap.read() #Leemos la captura del video
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame= gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        #LBPHFace:
        if result[1]< 70:    
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            



    frame = detector.encontrarmanos(frame) #Llamamos el objeto que contiene la calse para la deteccion
    lista, bbox = detector.encontrarposicion(frame, dibujar=False)#Llamamos la posicion de los putnos que necesitamos
    if len(lista) != 0 : #Si hay algo en la lista lo vamos a imprimir en este caso el punto 4 y el punto 8
        #print(lista[4], lista[8]) #Estos puntos pertenecen a la punta del dedo pulgar y dedo indice
        x1,y1 = lista[4][1], lista[4][2]#Encontramos la coordenada x e y del pulgar
        x2,y2 = lista[8][1], lista[8][2]#Encontramos la coordenada x e y del indice

        #---------Vamos a comprobar q el dedo indice y el dedo pulgar esten arriba
        dedos = detector.dedoarriba()
        #print(dedos)

        #------Nos aseguramos de que los dedos esten arriba
        if dedos[0] == 1 and dedos[1] == 1:
            longitud, frame, linea = detector.distancia(4,8,frame, r=8, t=2)
            print(longitud)

            #Nuestro
            #rango de manos es 25 hasta 200
            #y el rango de volumen es de ... hasta ....
            vol = np.interp(longitud,[20,160],[VolMin,VolMax])
            #print(vol)
            volumen.SetMasterVolumeLevel(vol, None)

            if longitud<25:
                cv2.circle(frame,(linea[4], linea[5]),10,(0,255,0),cv2.FILLED)

    cv2.imshow("Video",frame)
    t =cv2.waitKey(1)

    if t==27:
        break
cap.release()
cv2.destroyAllWindows()

