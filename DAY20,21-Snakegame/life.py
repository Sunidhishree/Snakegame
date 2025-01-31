
from turtle import Turtle
import random

class Lives(Turtle):

    def __init__(self):
        super(). __init__()
        self.color("red")
        self.penup()
        self.goto(0,250)
        self.write("<3<3<3", align="center", font=("Arial", 12, "bold"))
        self.hideturtle()

    def decrease(self):
        self.clear()
        self.write("<3<3", align="center", font=("Arial", 12, "bold"))

    def decrease_again(self):
        self.clear()
        self.write("<3", align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.clear()
