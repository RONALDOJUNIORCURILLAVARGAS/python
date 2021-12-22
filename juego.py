import turtle
import time 
import random

posponer=0.05 
#marcador
score=0
high_score=0

#configuracion de la ventana
wn=turtle.Screen()
wn.title("Juego de la serpiente")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
 

#comida serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#estado para evitar retroceder
#estado = turtle.Turtle()
#estado.direction = "stop"

#Segmentos/ cuerpo de la serpiente
segmentos = []
#Texto 
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
#texto.write("Score:   0  High Score:   0",align="center",font=("Courier",24,"normal"))
#funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"  
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right" 


estado= "stop"


def mov(estado):
    validacion=False
    if cabeza.direction =="up" and estado!="down":

        y = cabeza.ycor()
        cabeza.sety(y + 20)
        validacion=True
    
    if cabeza.direction =="down" and estado != "up":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        validacion=True

    if cabeza.direction =="left" and estado != "right":
        x = cabeza.xcor()
        cabeza.setx (x - 20)
        validacion=True
    
            
    if cabeza.direction =="right" and estado != "left":
        x = cabeza.xcor()
        cabeza.setx (x + 20)
        validacion=True

    if validacion==False:
        cabeza.direction=estado

   


#teclado 
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")
wn.onkeypress(arriba,"w")
wn.onkeypress(abajo,"s")
wn.onkeypress(izquierda,"a")
wn.onkeypress(derecha,"d")
wn.onkeypress(arriba,"W")
wn.onkeypress(abajo,"S")
wn.onkeypress(izquierda,"A")
wn.onkeypress(derecha,"D")



while True:
    wn.update()
      
    texto.clear()
    texto.goto(0,260)
    texto.write("Score:  {}  High Score:  {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 230 or cabeza.ycor() < -280:
         time.sleep(1)
         cabeza.goto(0,0)
         cabeza.direction = "stop"
         estado="stop"
        #Esconder los segmentos pintadolos de negro
         for segmento in segmentos:
            segmento.goto(1000,1000)
           
        #limpiando segmentos    
         segmentos.clear()
        #reseteando el score 
         score=0

   
    #Colisiones comida
    #20pixeles 

    #Generar nueva comida
    if cabeza.distance(comida)< 20:
        x=random.randint(-280,280)
        y=random.randint(-280,230)
        comida.goto(x,y)
        #aumentando la cola de la snake
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        #agregar valor de marcador
        score +=10
        if score > high_score:
            high_score=score
        #texto.goto(0,260)
        #texto.write("Score:  {}  High Score:  {}".format(score,high_score),align="center",font=("Courier",24,"normal"))    

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x= segmentos[index-1].xcor()
        y= segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg >0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)

    
     
    
    mov(estado)
    estado=cabeza.direction

    #colisiones cuerpo

    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            estado="stop"
            #esconder segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()
            score=0 
        



    time.sleep(posponer)
input()