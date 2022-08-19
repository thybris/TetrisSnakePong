import re
import turtle

class Goal:
    def goalBoarder(self):
        goal=turtle.Turtle()
        goal.shape("square")
        goal.goto(-500,0)
        goal.shapesize(stretch_wid = 50, stretch_len = 0.5)
        return goal