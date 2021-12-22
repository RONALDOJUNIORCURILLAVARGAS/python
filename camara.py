import math
import cv2
import time
#------------------Funcion principal
def main():
    ptiempo = 0
    ctiempo = 0
    #----------Leemos la camara web
    cap = cv2.VideoCapture(0)
  
    while True:
        ret,frame = cap.read()
        #calculo de los fps
        ctiempo = time.time()
        fps= 1 / (ctiempo - ptiempo)
        ptiempo = ctiempo

        cv2.putText(frame, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255),3)
        cv2.imshow("Manos",frame)
        k = cv2.waitKey(1)
        if k == 27 :
            break
    cap.release()
    cv2.destroyAllWindows()

main()


