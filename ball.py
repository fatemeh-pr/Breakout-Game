from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_step = 10
        self.y_step = 10
        self.move_delay = 0.1
        self.hit_upper_wall = False

    def move(self):
        new_xcor = self.xcor() + self.x_step
        new_ycor = self.ycor() + self.y_step
        self.goto(new_xcor, new_ycor)

    def bounce_horizontal(self):
        self.x_step *= -1

    def bounce_vertical(self):
        self.y_step *= -1

    def increase_speed(self):
        self.move_delay /= 1.3

    def go_home(self):
        self.x_step = random.choice([-10, 10])
        self.y_step = random.choice([-10, 10])
        self.goto(0, 0)

    def restart(self):
        self.goto(0, 0)
        self.x_step = 10
        self.y_step = 10
        self.move_delay = 0.1
        self.hit_upper_wall = False
