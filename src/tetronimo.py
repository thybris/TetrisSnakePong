import turtle
import random

class Tetronimo:
    
      def __init__(self):
        self.x = 5
        self.y = 0
        self.color = "black"
        
        # Block Shape
        square = [[1,1],
                  [1,1]]

        horizontal_line = [[1,1,1,1]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]

        left_l = [[1,0,0,0],
                  [1,1,1,1]]
                   
        right_l = [[0,0,0,1],
                   [1,1,1,1]]
                   
        left_s = [[1,1,0],
                  [0,1,1]]
                  
        right_s = [[0,1,1],
                   [1,1,0]]
                  
        t = [[0,1,0],
             [1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        # Choose a random shape each time
        self.shape = random.choice(shapes)

        print("test")

                      
        self.height = len(self.shape)
        self.width = len(self.shape[0])

    