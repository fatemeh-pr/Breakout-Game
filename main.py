import time
from ball import Ball
from bricks import Bricks
from paddle import Paddle
from score_board import ScoreBoard
from turtle import Screen

screen = Screen()
screen.setup(height=700, width=500)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
score_board = ScoreBoard()
bricks = Bricks()

screen.listen()
screen.onkey(paddle.to_right, "Right")
screen.onkey(paddle.to_left, "Left")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_delay)

    # Detect paddle missing the ball
    if ball.ycor() <= -330:
        ball.go_home()
        score_board.update_turns()

    # Detect collision with walls
    if ball.xcor() < -220 or ball.xcor() > 220:
        ball.bounce_horizontal()

    # Detect collision with paddle
    if abs(ball.xcor() - paddle.xcor()) <= 40 and abs(ball.ycor() - paddle.ycor()) < 25:
        ball.bounce_vertical()

    # Detect collision with upper wall & shrink the paddle
    if 320 < ball.ycor() < 340:
        ball.bounce_vertical()
        if not ball.hit_upper_wall:
            paddle.shrink_paddle()
            ball.hit_upper_wall = True

    # Detect collision with bricks
    for brick in bricks.all_bricks[:]:
        if abs(ball.xcor() - brick.xcor()) <= 15 and abs(ball.ycor() - brick.ycor()) < 18:
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            bricks.hit_brick()
            score_board.update_score(brick.score)
            ball.bounce_vertical()

            # Increase ball speed
            if bricks.hits in (4, 12):
                ball.increase_speed()
            elif brick.color()[0] == "orange" and not bricks.hit_orange:
                ball.increase_speed()
                bricks.hit_orange = True
            elif brick.color()[0] == "red" and not bricks.hit_red:
                ball.increase_speed()
                bricks.hit_red = True

    # Check score
    if not bricks.all_bricks and bricks.bricks_set == 1:
        bricks.create_brick()
        ball.restart()
        paddle.restart()

    if score_board.score == bricks.total_score * 2:
        score_board.announce_winner()
        if ball.ycor() < -330:
            ball.bounce_vertical()

    # Check turns
    if score_board.turns_over():
        game_on = False
        print("Game Over!")

screen.exitonclick()
