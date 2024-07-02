from turtle import Turtle
from random import randint

class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.color("red")
        self.food.shapesize(2)

    def position(self):
        self.food.goto(x=randint(-250, 250), y=randint(-250, 250))
