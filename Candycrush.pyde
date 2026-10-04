#Pasit Nualprasertsuk 69-010126-1030-7 20
import random
import os

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
                    self.grid[i][j] = random.randint(1,4)
                j = j + 1
            i = i + 1
    
    def save_board(self, filename="savegame.txt"):
        lines = []
        i = 0
        while i < self.row:
            row_str = ""
            j = 0
            while j < self.column:
                candy = self.grid[i][j]
                char = "R"

                if candy != None:
                    if candy == 1:
                        char = "R"
                    elif candy == 2:
                        char = "G"
                    elif candy == 3:
                        char = "B"
                    elif candy == 4:
                        char = "Y"

                row_str = row_str + char
                j = j + 1

            lines.append(row_str)
            i = i + 1

        saveStrings(filename, lines)
        println("Saved successfully")
    
    def load_board(self, filename="savegame.txt"):
        lines = loadStrings(filename)
        if lines == None:
            println("Error: Save file not found!")
            return

        i = 0
        while i < self.row and i < len(lines):
            line_data = lines[i].strip()
            j = 0
            while j < self.column and j < len(line_data):
                char = line_data[j]
                tmp = 1

                if char == "R":
                    tmp = 1
                elif char == "G":
                    tmp = 2
                elif char == "B":
                    tmp = 3
                elif char == "Y":
                    tmp = 4
                    
                self.grid[i][j] = tmp
                j = j + 1
            i = i + 1

        println("Loaded successfully")
                    
    def three_del(self):
        delete = []
        i = 0
        while i < len(self.grid):
            row = []
            j = 0
            while j < len(self.grid):
                row.append(False)
                j = j + 1
            delete.append(row)
            i = i + 1
        #Build grid to delete
        
        i = 0
        while i < self.row:
            j = 0
            while j < self.column:
                tmp = self.grid[i][j]
                if tmp != 0 and tmp == self.grid[i][j+1] and tmp == self.grid[i][j+2]: #check next pos and another next pos in x axis
                    delete[i][j] = True
                    delete[i][j+1] = True
                    delete[i][j+2] = True
                j = j + 1
            i = i + 1
                    
        i = 0
        while i < self.row:
            j = 0
            while j < self.column:
                tmp = self.grid[i][j]
                if tmp != 0 and tmp == self.grid[i+1][j] and tmp == self.grid[i+2][j]: #check next pos and another pos i y axis
                    delete[i][j] = True
                    delete[i+1][j] = True
                    delete[i+2][j] = True
                j = j + 1
            i = i + 1
            
        i = 0
        while i < self.row:
            j = 0
            while j < self.column:
                if delete[i][j] == True:
                    self.grid[i][j] = 0
                j = j + 1
            i = i + 1
            
    def fall(self):
        j = 0
        while j < self.column:
            i = self.row - 1
            
            while i >= 0:
                if self.grid[i][j] == 0:
                    k = i - 1
                    above = False
                    while k >= 0:
                        if self.grid[k][j] != 0:
                            self.grid[i][j] = self.grid[k][j]
                            self.grid[k][j] = 0
                            above = True
                            break
                        k = k - 1
                    if above == False:
                        self.grid[i][j] = random.randint(1,4)
                i = i - 1
            j = j + 1
                    
class Game(object):
    def __init__(self,scr_x = 500,scr_y = 500):
        self.scr_size = (scr_x, scr_y)
        self.board = Board(10,10)
        self.grid_per_sqr = scr_x // self.board.column
        self.click = [] 
    
    def settings(self):
        size(self.scr_size[0], self.scr_size[1])
        
    def setup(self):
        stroke(2)
        strokeWeight(3)
        self.board.get_candy()
        self.board.fillin()
    
    def visual(self):
        stroke(210)
        strokeWeight(1)
        
        j = 0
        while j <= self.board.column:
            x = j * self.grid_per_sqr
            line(x,0,x, self.scr_size[1])
            j = j + 1
        
        i = 0
        while i <= self.board.row:
            y = i * self.grid_per_sqr
            line(0,y,self.scr_size[0],y)
            i = i + 1
        
        d = self.grid_per_sqr * 0.8
        
        i = 0
        while i < self.board.row:
            j = 0
            while j < self.board.column:
                tmp = self.board.grid[i][j]
                if tmp != 0:
                    if tmp == 1:
                        fill(255, 0, 0)  
                    elif tmp == 2:
                        fill(0, 255, 0)  
                    elif tmp == 3:
                        fill(0, 0, 255)  
                    elif tmp == 4:
                        fill(240, 200, 60)
                        
                    cx = (j * self.grid_per_sqr) + (self.grid_per_sqr // 2)
                    cy = (i * self.grid_per_sqr) + (self.grid_per_sqr // 2)
                    
                    noStroke()
                    ellipse(cx, cy, d, d)
                j = j + 1
            i = i + 1
        if len(self.click) == 1:
            click_y = self.click[0][0]
            click_x = self.click[0][1]
            cx = (click_x * self.grid_per_sqr) + (self.grid_per_sqr // 2)
            cy = (click_y * self.grid_per_sqr) + (self.grid_per_sqr // 2)

            noFill()
            stroke(255, 50, 50)
            strokeWeight(3)
            ellipse(cx, cy, d + 20, d + 20)
                    
    def mousePressed(self):
        x = mouseX // self.grid_per_sqr
        y = mouseY // self.grid_per_sqr
        
        if y < self.board.row and x < self.board.column:
            self.click.append([y,x])
            
            if len(self.click) == 2:
                pos1 = self.click[0]
                pos2 = self.click[1]
                
                y1 = pos1[0]
                x1 = pos1[1]
                y2 = pos2[0]
                x2 = pos2[1]
                
                is_near = (abs(y1-y2) + abs(x1-x2)) == 1
                
                if is_near:
                    tmp = self.board.grid[y1][x1]
                    self.board.grid[y1][x1] = self.board.grid[y2][x2]
                    self.board.grid[y2][x2] = tmp
                self.click = []
    
    def keyPressed(self):
        if key == "s" or key == "S":
            self.board.save_board("savegame.txt")
        elif key == "l" or key == "L":
            self.board.load_board("savegame.txt")
                    
    def draw(self):
        background(245)
        self.board.three_del()
        self.board.fall()
        self.visual()
        
game = Game(500,500)

def settings():
    game.settings()

def setup():
    game.setup()
    
def draw():
    game.draw()

def mousePressed():
    game.mousePressed()

def keyPressed():
    game.keyPressed()
