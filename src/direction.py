import turtle

class Move:
    def move(self, snakehead):
        if snakehead.direction == "right":
            x = snakehead.xcor()
            snakehead.setx(x + 3)
        if snakehead.direction == "left":
            x = snakehead.xcor()
            snakehead.setx(x -3)
        if snakehead.direction == "up":
            y = snakehead.ycor()
            snakehead.sety(y + 3)
        if snakehead.direction == "down":
            y = snakehead.ycor()
            snakehead.sety(y - 3)
        
class Input:
    def __init__(self, screen, head, defender):
        self.screen = screen
        self.head = head
        self.defender = defender
        
    def keyboard_bindings(self):
        self.screen.listen()
        
        
        self.screen.onkeypress(self.snakeRight, "Right")
        self.screen.onkeypress(self.snakeLeft, "Left")
        self.screen.onkeypress(self.snakeUp, "Up")
        self.screen.onkeypress(self.snakeDown, "Down") 
        self.screen.onkeypress(self.defenderUp, "z")
        self.screen.onkeypress(self.defenderDown, "s")

    def snakeUp(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    
    def snakeDown(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    
    def snakeLeft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def snakeRight(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    
    def defenderUp(self):
        y = self.defender.ycor()
        y += 3
        self.defender.sety(y)
    
    def defenderDown(self):
        y = self.defender.ycor()
        y-= 3
        self.defender.sety(y)
    
    
    