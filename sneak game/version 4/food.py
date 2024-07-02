import random
import time
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        if random.randint(1, 100) >= 80:
            self.color("red")
        else:
            self.color("blue")

        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
