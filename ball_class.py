from random import choice
import turtle

directions = [240, 300]

class Ball(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.penup()
        self.color('azure1')
        self.setposition(0, 0)
        self.setheading(choice(directions))

    def move(self):
        self.forward(15)

    def bounce_wall(self):
        self.setheading(360 - self.heading() + 180)

    def bounce_horizontal(self):
        self.setheading(360 - self.heading())

    def bounce(self):
        self.setheading(choice(range(30, 150)))

    def reset(self):
        self.setposition(0, 0)
        self.setheading(choice(directions))