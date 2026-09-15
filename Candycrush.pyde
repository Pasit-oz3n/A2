#Pasit Nualprasertsuk 69-010126-1030-7 20
import random

grid_s = [10,10]
scr_size = [500,500]

g = []
def get_candy(grid,grid_size):
    i = 0
    while i < grid_size[0]+3:
        gridy = []
        j = 0
        while j < grid_size[1]+3:
            gridy.append(0)
            j = j + 1
        i = i + 1
        
def setup():
    size(scr_size[0],scr_size[1])
    stroke(2)
    strokeWeight(3)
    get_candy(g,grid_s)

def fillin(grid_x,grid_y,matrix):
    y = 0
    while y < grid_y:
        i = 0
        while i < grid_x:
            if matrix[y][x] == 0:
                matrix[y][x] = random.randint(1,4)
            x = x + 1
        y = y + 1
    

def visual(grid_x,grid_y,scr_sizex,scr_sizey,matrix):
    colour = [[255,0,0],
              [0,255,0],
              [0,0,255],
              [255,0,255]]
    
    
    

#def three_del(grid_x,grid_y,matrix):
    

#def fall(grid_x,grid_y,matrix):
    
#def mousePressed():
        

def draw():
    background(255)
    
    
