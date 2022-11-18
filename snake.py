##Se importan las librerias necesarias
from turtle import Turtle
# Se establecen las posiciones iniciales de la serpiente y los angulos en que se va a mover
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# Se crea una clase llamada snake
class Snake:
    # Se usa el metodo __init__ para inicializar los atributos del metodo
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    #Se establece la posicion en la que se va a crear la serpiente
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    #Se establecen las caracteristicas de la serpiente, el color, la forma, la poscion, etc. 
    def add_segment(self, position):
        new_segment = Turtle("square",10)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    # Se usa para añadir un segmento cada que la serpiente come esta se añade en la posicion anterior a la primera
    def extend(self):
        self.add_segment(self.segments[-1].position())
    # Se establece la direccion del movimineto dependiento de los ejes x, y 
    def move(self):
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    #Se pone el angulo en el que se va mover en caso de presionar un boton
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    #Se pone el angulo en el que se va mover en caso de presionar un boton
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #Se pone el angulo en el que se va mover en caso de presionar un boton
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    #Se pone el angulo en el que se va mover en caso de presionar un boton
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)