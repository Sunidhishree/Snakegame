import turtle
from turtle import Turtle,Screen
import random
import time
from snake import Snake
from food import Food
from score import Score
from life import Lives
l=3
s=0
t=0.2
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food=Food()
score = Score()
lives = Lives()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(t)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()
        s+=1
        if s>=10:
            t=0.15
        elif s>=20:
            t=0.1
        elif s>=30:
            t=0.08
        elif s>=40:
            t=0.05

    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 250 or snake.head.ycor() <-290:
        score.highscore()
        score.high()
        game_is_on=False
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            l-=1
            if l==2:
                lives.decrease()
            elif l==1:
                lives.decrease_again()
            elif l==0:
                lives.game_over()
                score.highscore()
                score.high()
                game_is_on=False


screen.exitonclick()