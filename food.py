#Se importan las librerias necesarias
from turtle import Turtle
import random

#Se establece una clase llamada food que recibe los objetos y metodos de turtle
class Food(Turtle):
    # Se usa el metodo __init__ para inicializar los atributos del metodo
    def __init__(self):
        super().__init__()
        # Se establece las caracteristicas de la comida, la forma, el tamaño, etc.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    #Se usa para que la comida aparezca de manera aleatoria dentro de los limites de la ventana
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)