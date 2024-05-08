import turtle

def dibujar_cuadrado(x, y, lado=20):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(lado)
        turtle.left(90)

def dibujar_circulo(x, y, radio=50):
    turtle.penup()
    turtle.goto(x, y - radio)
    turtle.pendown()
    turtle.circle(radio)
