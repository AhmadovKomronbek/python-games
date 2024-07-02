from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update(self):
        self.write(f"Score {self.score}", align="center")

    def game_over(self, best_score):
        self.goto(0, 40)
        self.color("black")
        self.write("GAME OVER", font=("Verdana", 24, "normal"), align="center")

        self.goto(0, 00)
        self.write(f"BEST SCORE {best_score}", font=("Verdana", 16, "normal"), align="center")

        self.goto(0, -40)
        self.write(f"YOUR SCORE SCORE {self.score}", font=("Verdana", 16, "normal"), align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def increase_score_more(self):
        self.score += 5
        self.clear()
        self.update()
