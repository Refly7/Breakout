from turtle import Turtle

class Lives(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.num = 3
        self.penup()
        self.setposition(-630, 350)
        self.color('white')
        self.hideturtle()
        self.refresh()
        
    def refresh(self):
        self.clear()
        self.write(f'{self.num}', False, 'center', ('Arial', 20, 'bold'))

    def game_over(self):
        self.setposition(0, -70)
        self.clear()
        self.write('Game Over', False, 'center', ('Arial', 50, 'bold'))
    
    def the_end(self):
        self.setposition(0, 0)
        self.clear()
        self.write('The End', False, 'center', ('Arial', 50, 'bold'))