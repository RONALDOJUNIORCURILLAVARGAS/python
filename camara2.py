import cv2
def mov():
    cap=cv2.VideoCapture(0)
    while(cap):
        ret, video= cap.read()
        if(ret):
            cv2.imshow("Prueba de camara", video)
            k=cv2.waitKey(1)
            #cerrar cuando selecciones escape(27) o espacio(32)
            
            if k== 27 or k==32 :
                break
    cap.release()
    cv2.destroyAllWindows()
mov()
