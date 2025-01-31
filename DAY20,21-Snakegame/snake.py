
from turtle import Turtle

import time

start = [(0, 0), (-20, 0), (-40, 0)]
m = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("DarkOliveGreen")
        self.head.shapesize(stretch_len=1.2, stretch_wid=1.2)
    def create_snake(self):
        for i in start:
           self.add(i)

    def add(self, i):
        new = Turtle("square")
        new.color('DarkOliveGreen1')
        new.penup()
        new.goto(i)
        self.segments.append(new)

    def extend(self):
        self.add(self.segments[-1].position())

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("DarkOliveGreen")
        self.head.shapesize(stretch_len=1.2, stretch_wid=1.2)

    def move(self):
        for j in range(len(self.segments) - 1, 0, -1):
            x = self.segments[j - 1].xcor()
            y = self.segments[j - 1].ycor()
            self.segments[j].goto(x, y)

        self.segments[0].forward(m)



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