import turtle
import time
import random
from snake import Snake, Tail
from direction import Move, Input
from goal import Goal
from defender import Defender
from tetronimo import Tetronimo, Check

delay = 0.1
score = 0
high_score = 0
startTail=1

screen = turtle.Screen()
screen.setup(width=1200, height=800)

head = Snake().snakehead()

tail = Tail()
snaketail=[]
snaketail = tail.AddingTail(snaketail)

Tetronimo = Tetronimo()
Check=Check()

directionMovement = Move()
directionMovement.move(head)

shape = turtle.Turtle()
#Tetronimo=Tetronimo()

goal=Goal().goalBoarder()
defender= Defender().defender()

keybinds = Input(screen, head, defender)
keybinds.keyboard_bindings()

    


while True:
    #snaketail = turtle.Turtle()  test showing tail
    #head = turtle.Turtle() #test showing head

    #tail.startOfTail(snaketail)
    
    #Tetronimo = turtle.Turtle()
    screen.update()
    Tetronimo.moveTetronimo()

    tail.startOfTail(snaketail)

    for i in range(len(snaketail)-1, 0, -1):
        x = snaketail[i-1].xcor()
        y = snaketail[i-1].ycor()
        snaketail[i].goto(x, y)

    if len(snaketail) > 0:
        x = head.xcor()
        y = head.ycor()
        snaketail[0].goto(x, y)

    if head.xcor() > 590 or head.xcor() < -450 or head.ycor() > 390 or head.ycor() < -390:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        Tetronimo.restartGame()
        snaketail.clear()



    
    

    directionMovement.move(head)
    Check.checkDefender(defender)

screen.mainloop()
