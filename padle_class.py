import turtle

class Padle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(1, 6)
        self.color('azure2')
        self.penup()
        self.setposition(0, -300)

    def move_right(self):
        if self.xcor() < 580:
            self.setheading(0)
            self.forward(30)

    def move_left(self):
        if self.xcor() > -580:
            self.setheading(180)
            self.forward(30)

    def reset(self):
        self.setposition(0, -300)