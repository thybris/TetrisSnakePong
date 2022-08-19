import turtle

class Snake:
    def snakehead(self):
        snakehead = turtle.Turtle()
        snakehead.shape("square")
        snakehead.color("green")
        snakehead.speed(40)
        snakehead.penup()
        snakehead.goto(0,0)
        snakehead.direction = "Right"
        return snakehead

class Tail:
    def __init__(self):
        self.startTail = 1

    def AddingTail(self, blocks):
        tailBlock = turtle.Turtle()
        tailBlock.shape("square")
        tailBlock.color("green")
        blocks.append(tailBlock)
        #test for showing tail
        #tailBlock.goto(10,10)

        return blocks

    def startOfTail(self, blocks):
        if self.tailLength == 1:
            for i in range (0,3):
                blocks = self.AddingTail(blocks)
            self.tailLength = 2
        return blocks