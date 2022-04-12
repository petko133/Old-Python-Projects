from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("cyan")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_left(self):
        x_left = self.xcor() - 20
        self.goto(x_left, self.ycor())

    def go_right(self):
        x_right = self.xcor() + 20
        self.goto(x_right, self.ycor())

