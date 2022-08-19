import turtle
import time
import random
from snake import Snake
from snakeTail import Tail
from tetronimo import Tetronimo
from direction import Move, Input

delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.setup(width=1000, height=600)

head = Snake().snakehead()
tail = Tail()
directionMovement = Move()
directionMovement.move(head)
snaketail=[]
snaketail = tail.AddingTail(snaketail)
#Tetronimo=Tetronimo()

keybinds = Input(screen, head)
keybinds.keyboard_bindings()


while True:
    #snaketail = turtle.Turtle()  test showing tail
    #head = turtle.Turtle() #test showing head

    #tail.startOfTail(snaketail)
    
    #Tetronimo = turtle.Turtle()
    screen.update()

    directionMovement.move(head)

screen.mainloop()
