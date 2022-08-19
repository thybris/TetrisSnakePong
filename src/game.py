import turtle
import time
import random
from snake import Snake

delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.setup(width=600, height=600)

head = Snake().snakehead()


while True:
    head = turtle.Turtle()

