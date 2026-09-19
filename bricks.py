from turtle import Turtle


class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.bricks_set = 0
        self.hits = 0
        self.total_score = 0
        self.hit_red = False
        self.hit_orange = False

        self.create_brick()
        self.cal_total_score()

    def create_brick(self):
        self.bricks_set += 1
        x_cor = -230
        y_cor = 300
        for (color, score) in [("red", 7), ("orange", 5), ("green", 3), ("yellow", 1)]:
            for i in range(28):
                brick = Turtle()
                brick.shape("square")
                brick.color(color)
                brick.score = score
                brick.shapesize(0.5, 1.5)
                brick.penup()
                brick.goto(x_cor, y_cor)
                self.all_bricks.append(brick)
                x_cor += 35
                if len(self.all_bricks) % 14 == 0:
                    y_cor -= 15
                    x_cor = -230

    def hit_brick(self):
        self.hits += 1

    def restart_bricks(self):
        self.all_bricks = []
        self.create_brick()
        self.hits = 0
        self.hit_red = False
        self.hit_orange = False

    def cal_total_score(self):
        self.total_score = sum([brick.score for brick in self.all_bricks])

