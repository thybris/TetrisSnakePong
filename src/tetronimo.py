import turtle

class Tetronimo:
    def __init__(self):
        self.tetronimo = turtle.Turtle()
        self.tetronimo = turtle.Turtle()
        self.tetronimo.shape("square")
        self.tetronimo.color("red")
        self.tetronimo.speed(40)
        self.tetronimo.penup()
        self.tetronimo.goto(-50,0)

    def moveTetronimo(self):
        #https://www.geeksforgeeks.org/turtle-xcor-function-in-python/
        self.tetronimo.setx(self.tetronimo.xcor() + 5)
        self.tetronimo.sety(self.tetronimo.ycor() + 5)