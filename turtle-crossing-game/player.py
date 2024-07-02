# TODO: Turtledan voris olib Player() nomli class yaratish
from turtle import Turtle

# TODO: oldinga yurish metodini qo'shish
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)

    def move_forward(self):
        self.forward(10)

    def move_back(self):
        self.backward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)
        self.setheading(90)

    def move_right(self):
        self.setheading(0)
        self.forward(10)
        self.setheading(90)

# TODO: agar keyingi levelga o'tsa turtleni boshlang'ich koyiga qaytarish
    def go_to_start(self):
        self.goto(x=0, y=-280)

    def finish_line(self):
        if self.ycor() > 280:
            return True
        return False
