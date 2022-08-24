import turtle

class Defender:
    def defender(self):
        defender=turtle.Turtle()
        defender.shape("square")
        defender.shapesize(stretch_wid = 6, stretch_len = 1)
        defender.penup()
        defender.goto(-450,0)
        defender.speed(0)
        return defender