from turtle import Turtle

class Target(Turtle):

    def __init__(self):
        super().__init__()
        self.all_target = []

    def create_target(self, x_cor, y_cor, color):
        new_target = Turtle("square")
        new_target.shapesize(stretch_wid=0.5, stretch_len=2)
        new_target.penup()
        new_target.color(color)
        new_target.goto(x_cor, y_cor)
        self.all_target.append(new_target)

    def hide(self):
        for n in self.all_target:
            n.hideturtle()
