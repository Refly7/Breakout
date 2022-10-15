import time
from turtle import Screen
from padle_class import Padle
from ball_class import Ball
from lives_class import Lives
from blocks_class import Blocks

screen = Screen()
screen.setup(width = 1300, height = 800)
screen.bgcolor('cyan4')
screen.title('Breakout Game')
screen.tracer(0)

game_on = True
lives = Lives()
padle = Padle()
ball = Ball()
blocks = Blocks()

screen.listen()
screen.onkey(padle.move_right,'Right')
screen.onkey(padle.move_left,'Left')

while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    
    if ball.xcor() < -630 or ball.xcor() > 630:
        ball.bounce_wall()

    if ball.ycor() > 380:
        ball.bounce_horizontal()

    if padle.distance(ball) < 70 and -300 < ball.ycor() < -275:
        ball.bounce()

    if ball.ycor() < -400:
        lives.num -= 1
        ball.reset()
        padle.reset()

        if lives.num < 0:
            lives.game_over()
            break
        lives.refresh()
        screen.update()
        time.sleep(1)

    for block in blocks.blocks:
        if abs(ball.xcor() - block.xcor()) < 50 and 20 < abs(ball.ycor() - block.ycor()) < 45:
            ball.bounce_horizontal()
            blocks.breaking(block)

        if 45 < abs(ball.xcor() - block.xcor()) < 60 and abs(ball.ycor() - block.ycor()) < 30:
            ball.bounce_wall()
            blocks.breaking(block)
    
    if len(blocks.blocks) == 0:
        lives.the_end()
        
screen.exitonclick()