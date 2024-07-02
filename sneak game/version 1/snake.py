from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.array_snake = []
        self.create_new_turtle()
        self.head = self.array_snake[0]
        self.head.color("green")

    # This method create new turtle and add snake list, when snake eat food
    def create_new_turtle(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green yellow")
            new_segment.penup()
            new_segment.goto(position)
            self.array_snake.append(new_segment)

    def create_new_turtle_element_in_array(self):
        new_segment = Turtle("square")
        new_segment.color("green yellow")
        new_segment.penup()
        self.array_snake.append(new_segment)

    def move(self):
        for seg_num in range(len(self.array_snake)-1, 0, -1):
            new_x = self.array_snake[seg_num - 1].xcor()
            new_y = self.array_snake[seg_num - 1].ycor()
            self.array_snake[seg_num].goto(new_x, new_y)
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
