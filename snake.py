from turtle import Turtle
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ['pink', 'blue', 'red', 'white', 'aqua', 'yellow', 'purple', 'green']


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape = 'arrow'


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def add_segment(self, position):

        new_segment = Turtle(shape='square')
        new_segment.color(COLORS[random.randint(0, 7)])
        new_segment.penup()
        new_segment.shapesize(stretch_wid=0.5)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        # add a new segment to the snake\
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor_next = self.segments[i - 1].xcor()
            y_cor_next = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor_next, y_cor_next)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
