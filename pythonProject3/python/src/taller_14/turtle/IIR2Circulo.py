import turtle
from funciones import dibujar_circulo

def dibujar_letra_I(x, y):
    for _ in range(5):
        dibujar_circulo(x, y)
        y -= 30

def dibujar_letra_P(x, y):
    dibujar_circulo(x, y)
    dibujar_circulo(x, y - 20)
    dibujar_circulo(x + 20, y - 20)
    dibujar_circulo(x + 20, y - 30)
    dibujar_circulo(x, y - 30)

def dibujar_circulo_y_circulo(x, y):
    dibujar_circulo(x, y, 10)
    dibujar_circulo(x + 40, y)

def main():
    turtle.speed(10)

    dibujar_letra_I(-150, 0)
    dibujar_letra_I(-100, 0)
    dibujar_letra_P(-50, 0)
    dibujar_circulo_y_circulo(0, 0)

    turtle.done()

if __name__ == "__main__":
    main()
