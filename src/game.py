import turtle
import time
import random
from snake import Snake
from snakeTail import Tail

delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.setup(width=600, height=600)

head = Snake().snakehead()
tail = Tail()
snaketail=[]
snaketail = tail.AddingTail(snaketail)


while True:
    head = turtle.Turtle()
    snaketail = turtle.Turtle()
