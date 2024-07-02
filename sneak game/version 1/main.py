from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

writer = Turtle()
writer.hideturtle()
writer.penup()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

food_box = Food()
food_box.position()
snake = Snake()

# Functions
def check_eat_food():
    food_x = float(food_box.food.xcor())
    food_y = float(food_box.food.ycor())
    snake_head_x = float(snake.array_snake[0].xcor())
    snake_head_y = float(snake.array_snake[0].ycor())
    if (round(abs(food_x - snake_head_x)) in num_array) and (round(abs(food_y - snake_head_y)) in num_array):
        return True
    return False

def check_border():
    for j in range(len(snake.array_snake)):
        if 300 <= snake.array_snake[j].xcor() or -300 >= snake.array_snake[j].xcor():
            return False
        elif 300 <= snake.array_snake[j].ycor() or -300 >= snake.array_snake[j].ycor():
            return False

        return True

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if check_eat_food():
        snake.create_new_turtle_element_in_array()
        food_box.position()

    elif not check_border():
        screen.clear()
        screen.bgcolor("red")
        writer.write("You lost", font=("Verdana", 32, "normal"), align="center")
        break

screen.exitonclick()
