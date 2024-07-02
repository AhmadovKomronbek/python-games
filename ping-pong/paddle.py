from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() + 75 <= 300:
            self.goto(y=self.ycor() + 25, x=self.xcor())

    def go_down(self):
        if self.ycor() - 75 >= -300:
            self.goto(y=self.ycor() - 25, x=self.xcor())
