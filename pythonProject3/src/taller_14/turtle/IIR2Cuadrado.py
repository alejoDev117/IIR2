import turtle
from funciones import dibujar_cuadrado

def dibujar_letra_I(x, y):
    for _ in range(5):
        dibujar_cuadrado(x, y)
        y -= 30

def dibujar_letra_P(x, y):
    dibujar_cuadrado(x, y)
    dibujar_cuadrado(x, y - 30)
    dibujar_cuadrado(x, y - 50)
    dibujar_cuadrado(x , y - 70)
    dibujar_cuadrado(x, y - 90)

def dibujar_numero_2(x, y):
    dibujar_cuadrado(x, y)
    dibujar_cuadrado(x + 20, y)
    dibujar_cuadrado(x, y - 20)
    dibujar_cuadrado(x, y - 30)
    dibujar_cuadrado(x + 20, y - 30)

def main():
    turtle.speed(11)

    dibujar_letra_I(-150, 0)
    dibujar_letra_I(-100, 0)
    dibujar_letra_P(-50, 0)
    dibujar_numero_2(0, 0)

    turtle.done()

if __name__ == "__main__":
    main()
