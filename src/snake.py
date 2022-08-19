import turtle

class Snake:
    def snakehead(self):
        snakehead = turtle.Turtle()
        snakehead.shape("square")
        snakehead.color("green")
        snakehead.speed(40)
        snakehead.penup()
        snakehead.goto(0,0)
        snakehead.direction = "Stop"
        return snakehead