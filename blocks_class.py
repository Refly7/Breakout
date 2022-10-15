import turtle

class Blocks():

    def __init__(self):
        self.blocks = []
        self.create_blocks()
        self.x = 0

    def create_blocks(self):
        for j in range(1, 5):
            for i in range(-6, 7):
                block = turtle.Turtle()
                block.shape('square')
                block.shapesize(2, 4.5)
                block.c = 'DarkOliveGreen' + f'{j}'
                block.color(block.c)
                block.penup()
                block.setposition(i * 100, j * 50)
                self.blocks.append(block)

    def breaking(self, n):
        if n.c == 'DarkOliveGreen1':
            n.hideturtle()
            self.x +=1
            print(self.x)
            self.blocks.pop(self.blocks.index(n))
        else:
            j = int(n.c[-1]) -1
            n.c = 'DarkOliveGreen' + f'{j}'
            n.color(n.c)