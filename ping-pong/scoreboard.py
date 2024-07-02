from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=280)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_player_score = 0
        self.l_player_score = 0
        self.write(f"{self.l_player_score} : {self.r_player_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_player_score} : {self.r_player_score}")

    def l_point(self):
        self.l_player_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_player_score += 1
        self.update_scoreboard()
