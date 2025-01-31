from turtle import Turtle
import random


colors=['CadetBlue2','coral','DeepPink','LightPink','lavender','LightBlue','MediumPurple1','tan']

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        q = random.randint(-270, 270)
        w = random.randint(-270, 240)
        self.color(random.choice(colors))
        self.goto(q, w)
