from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()
best_score = 0

flag = True
while flag:
    food = Food()
    writer = ScoreBoard()

    game_mode_snake_speed = 0

    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    while True:
        game_mode = screen.textinput("CHOOSE GAME MODE", "Please enter game mode(normal, hard)")

        if game_mode in ["normal", "hard"]:
            if game_mode == "hard":
                game_mode_snake_speed = 0.05
            else:
                game_mode_snake_speed = 0.1
            break

    snake = Snake()

    screen.listen()

    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(game_mode_snake_speed)
        snake.move()
        writer.update()

        if snake.head.distance(food) < 30:
            food.refresh()

            snake.extend()
            if food.color() == ("blue", "blue"):
                writer.increase_score()
            else:
                writer.increase_score_more()


        if 280 < snake.head.xcor() or -280 > snake.head.xcor() or 280 < snake.head.ycor() or -280 > snake.head.ycor():
            game_is_on = False
            screen.clear()
            if best_score <= writer.score:
                best_score = writer.score
            writer.game_over(best_score)

            time.sleep(3)
            while True:
                game_mode = screen.textinput("PLAY AGAIN?", "Do you want play again ?(yes or no)")

                if game_mode in ["yes", "no"]:
                    if game_mode == "no":
                        flag = False
                        break

                    writer.score = 0
                    break


        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                screen.clear()
                if best_score <= writer.score:
                    best_score = writer.score
                writer.game_over(best_score)
                time.sleep(3)

                while True:
                    game_mode = screen.textinput("PLAY AGAIN?", "Do you want play again ?(yes or no)")

                    if game_mode in ["yes", "no"]:
                        if game_mode == "no":
                            flag = False
                            break

                        writer.score = 0
                        break

screen.exitonclick()
