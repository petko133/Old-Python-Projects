from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, -140)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    def scoreboard(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.update_score()
        self.goto(0, -50)
        self.write("Game Over", align="center", font=("Courier", 40, "normal"))

