import turtle

class Move:
    def move(self, snakehead):
        if snakehead.direction == "right":
            x = snakehead.xcor()
            snakehead.setx(x + 10)
        if snakehead.direction == "left":
            x = snakehead.xcor()
            snakehead.setx(x -10)
        if snakehead.direction == "up":
            y = snakehead.ycor()
            snakehead.sety(y + 10)
        if snakehead.direction == "down":
            y = snakehead.ycor()
            snakehead.sety(y - 10)
        
class Input:
    def __init__(self, screen, head):
        self.screen = screen
        self.head = head
        
    def keyboard_bindings(self):
        self.screen.listen()
        self.screen.onkeypress(self.snakeRight, "Right")
        self.screen.onkeypress(self.snakeLeft, "Left")
        self.screen.onkeypress(self.snakeUp, "Up")
        self.screen.onkeypress(self.snakeDown, "Down")

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
    

    
    
    