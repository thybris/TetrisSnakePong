import turtle

class Tetronimo:
    def __init__ (self):
        self.tetronimo = turtle.Turtle()
        self.tetronimo.shape("square")
        self.tetronimo.color("red")
        self.tetronimo.speed(80)
        self.tetronimo.penup()
        self.tetronimo.goto(-50,0)
        self.tetronimo.moveHorizontal = 5
        self.tetronimo.moveVertical = 5

    def moveTetronimo(self):
        #https://www.geeksforgeeks.org/turtle-xcor-function-in-python/
        
        self.tetronimo.setx(self.tetronimo.xcor() + self.tetronimo.moveHorizontal)
        self.tetronimo.sety(self.tetronimo.ycor() + self.tetronimo.moveVertical)
        Check.checkWall(self)

    def restartGame(self):
        self.tetronimo.goto(0,0)
        

class Check (Tetronimo):
    def checkWall(self):

        #upper wall
        if self.tetronimo.ycor() > 400:
            self.tetronimo.sety(400)
            self.tetronimo.moveVertical *= -1

        #right wall
        if self.tetronimo.xcor() > 600:
            self.tetronimo.setx(600)
            self.tetronimo.moveHorizontal *= -1

        #lower wall
        if self.tetronimo.ycor() < -400:
            self.tetronimo.sety(-400)
            self.tetronimo.moveVertical *= -1

        #corner check upper
        if self.tetronimo.ycor() > 400 & self.tetronimo.xcor() > 600:
            self.tetronimo.sety(400)
            self.tetronimo.setx(600)
            self.tetronimo.moveVertical *= -1
            self.tetronimo.moveHorizontal *= -1

        #corner check lower
        if self.tetronimo.ycor() < -400 & self.tetronimo.xcor() > 600:
            self.tetronimo.sety(-400)
            self.tetronimo.setx(600)
            self.tetronimo.moveVertical *= -1
            self.tetronimo.moveHorizontal *= -1

    def checkWin(self):
        if self.tetronimo.xcor() < -500:
            self.tetronimo.setx(-500)
            #test bounce --> self.tetronimo.moveHorizontal *= -1

    def checkDefender(self,defender):
        if(self.tetronimo.xcor() < - 450 and self.tetronimo.xcor() > -460 and ((self.tetronimo.ycor() < defender.ycor() + 50)and(self.tetronimo.ycor() < defender.ycor() - 50))):
            self.tetronimo.setx(-450)
            self.tetronimo.moveHorizontal *= -1


    