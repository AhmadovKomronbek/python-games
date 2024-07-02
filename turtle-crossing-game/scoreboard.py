# TODO: Turtledan meros olib score tab yaratish
# TODO: gamer_over() va update_scoreboard() metodini qo'shish
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-220, y=260)
        self.write(f"Level {self.level}", align="center", font=("normal", 20, "bold"))
        self.level += 1

    def game_over(self, best_score, game_mode_name):
        self.goto(x=0, y=30)
        self.write("YOU LOSE", align="center", font=("normal", 24, "bold"))
        self.goto(x=0, y=-30)
        self.write(f"BEST SCORE: {best_score} (game mode: {game_mode_name})", align="center", font=("normal", 24, "bold"))
