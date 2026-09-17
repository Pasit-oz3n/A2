#Pasit Nualprasertsuk 69-010126-1030-7 20
import random

class Candy(object):
    def __init__(self,type_id,x,y):
        self.type_id = type_id
        self.x = x
        self.y = y
        self.is_select = False

class Board(object):
    def __init__(self, column = 10 , row = 10):
        self.column = column
        self.row = row
        self.grid = []
        self.candy = [Candy(0,x,y)]
        
    def get_candy(self):
        self.grid = []
        i = 0
        while i < self.row + 3:
            row_grid = []
            j = 0
            while j < self.column + 3:
                row_grid.append(0)
                j = j + 1
            self.grid.append(row_grid)
            i = i + 1
    
    def fillin(self):
        i = 0
        while i < self.row:
            j = 0
            while j < self.column:
                if self.grid[i][j] == 0:
                    self.grid[i][j] == random.randint[1,4]
                j = j + 1
            i = i + 1
    #def fall(self):
        
            
    #def three_del(self):
        #i = 0

class Game(object):
    def __init__(self,scr_x = 500,scr_y = 500):
        self.scr_size = (scr_x, scr_y)
        self.board = Board(10,10)
        self.grid_per_sqr = scr_x // self.board.column
        
    def setup(self):
        size(self.scr_size[0],self.scr_size[1])
        stroke(2)
        strokeWeight(3)
        self.board.get_candy()
    
   '''def draw():
       background(240)
       self.board.fillin()
       self.board.fall()
      ''' 

board_size = Board(10,10)
    
    
