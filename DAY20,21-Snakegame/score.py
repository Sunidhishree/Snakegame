import turtle
from turtle import Turtle
import random

class Score(Turtle):

    def __init__(self):
        super(). __init__()
        self.s=0
        with open ("data.txt") as data:
            self.hs = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.s} Highscore: {self.hs}", align="center", font=("Arial", 14, "normal"))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.s += 1
        self.write(f"Score: {self.s} Highscore: {self.hs}", align="center", font=("Arial", 14, "normal"))

    def high(self):
        if self.s>self.hs:
            self.hs = self.s
        with open("data.txt", mode="w") as data:
            data.write(str(self.hs))

    def highscore(self):
        self.clear()
        self.goto(0, 10)
        if self.s > self.hs:
            self.clear()
            self.goto(0,-10)
            self.write(f"              GAME OVER\nYou created a new Highscore {self.s}", align="center", font=("Arial", 14, "normal"))
        else:
            self.write(f"   GAME OVER\nYour score: {self.s}\nHigh Score: {self.hs}", align="center", font=("Arial", 14, "normal"))