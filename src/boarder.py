class Boarder():
    #https://github.com/wynand1004/Projects/blob/master/Space%20Arena/space_arena_7.py
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def render_border(self, pen):
        pen.color("green")
        pen.width(3)
        pen.penup()
        
        left = -self.width
        right = self.width
        top = self.height
        bottom = -self.height
        
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    def border_check(self):
        if self.x > self.width - 10:
            self.x = self.width - 10
            self.dx *= -1
            
        elif self.x < -self.width + 10:
            self.x = -self.width+ 10
            self.dx *= -1

        if self.y > self.height- 10:
            self.y = self.height - 10
            self.dy *= -1
            
        elif self.y < -self.height+ 10:
            self.y = -self.height + 10
            self.dy *= -1   