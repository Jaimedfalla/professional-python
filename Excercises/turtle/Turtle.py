import turtle

screen = turtle.Screen() # Se crea un lienzo de turtle
t = turtle.Turtle() # Ubica la tortuga en las coordenadas 0,0
t.shape("turtle") #Cambia la forma de la tortuga (arrow,circle, square,triangle,classic)
#t.speed(1) # Asigna la velocida de dibujo a la tortuga, solo toma valores del 1 al 10
# screen.bgcolor("green") #Modifica el color del lienzo
# screen.title("Project 1")
# t.shapesize(10,5,1) #Modifica el tamaño de la tortuga
# t.fillcolor("orange")
# t.pencolor("white") #Cambia el color del borde a blanco
# t.color("blue","blue") #Modifica el color del borde y el relleno de la tortuga
# t.pensize(5)#Modifica el grosor del tinta
# t.backward(100) # Mueve la tortuga hacia atrás
# t.right(90) # Rota la tortuga hacia la derecha. Es equivalente al comando rt(90)
# t.forward(100) # Mueve la tortuga hacia adelante. También se puede utilizar el comando fd(100)
# t.left(90) # Rota la tortuga hacia la izquierda
# t.goto(-100,100) # Ubica a la tortuga en las coordenadas X=-100 y Y=100
# t.home() #Ubica a la tortuga en las coordenadas 0,0
# t.circle(50) # Dibuja un círculo de radio 50
# t.dot(30) # Dibuja un punto de diámetro 30
# t.hideturtle() # Oculta la tortuga
# t.showturtle() # Muestra la tortuga si está oculta
# t.begin_fill() #Dibuja un circulo relleno
# t.circle(100)
# t.end_fill()

# t.begin_fill()
# t.color("white","white")
# t.circle(50)
# t.end_fill()
# t.penup() #Para que no se dibuje el trazo del movimiento
# t.pendown() #Para que vuelva a dibujar el trazo
# t.clear() # Limpia toda la pantalla
# t.undo() # Deshace el último movimiento
# t.reset() # Reinicia la pantalla
# t.stamp() # Deja un sello en el camino
turtle.done() # Deja el liezo fijo