#Se importan las librerias necesarias
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


#Se establece una clase llamada Scoreboard que recibe los objetos y metodos de turtle
class Scoreboard(Turtle):
    # Se usa el metodo __init__ para inicializar los atributos del metodo
    def __init__(self):
        super().__init__()
        #Se establecen las caracteristicas del score el color de la letra, donde se va a ubicar y se llama el metodo update_scoreboard
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    # Se crea el metodo update_scoreboard para concatenar el puntaje a  el score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)    
    # Se usa para mostrar en medio de la pantalla un mensaje que diga que el juego se acabo
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #Se usa para que dentro de una variable se almacene el conteo del score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()