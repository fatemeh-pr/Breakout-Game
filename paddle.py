from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4)
        self.penup()
        self.goto(0, -320)

    def to_right(self):
        self.forward(10)

    def to_left(self):
        self.back(10)

    def shrink_paddle(self):
        self.shapesize(1, 2)

    def restart(self):
        self.shapesize(1, 4)
