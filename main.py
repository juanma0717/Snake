# Se importan las librerias y los archivos necesarios para el funcionamiento del juego.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Se establecen todas las propiedades de la ventana donde se ejecutara el juego
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Se usan variables para llamar la clases y 
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Se usan metodos para hacer que la ventana capte diferentes acciones que hacen los botones
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Se usa esta variable para que el sistema tenga en cuenta si el juego esta activo
game_is_on = True
#Si el juego esta activo se ejecutara todo lo que contiene el bucle while
while game_is_on:
    #Se actualiza la pantalla cada cierto tiempo
    screen.update()
    time.sleep(0.2)
    #Llama de la clasa snake el metodo move
    snake.move()
    #Se llaman diferentes metodos de kas difrentes clases importadas para que el la serpiente, la comida y el score se actualizen
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Se establece que si la serpiente toca los bordes de la ventana el juego se acaba
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # Si algunos de los segmentos se tocan se acaba el juego
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
# Solo  si el juego se acaba se cerrara la ventana si se hace click sobre esta misma
screen.exitonclick()