import turtle

class Tail:
    def __init__(self):
        self.startTail = 1

    def AddingTail(self, blocks):
        tailBlock = turtle.Turtle()
        tailBlock.shape("square")
        tailBlock.color("green")
        blocks.append(tailBlock)
        #test for showing tail
        tailBlock.goto(10,10)

        return blocks