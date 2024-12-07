file = open("./data.txt", "r")
cells = [list(line.strip()) for line in file.readlines()]
walkingPath = cells.copy()



def findStart():
    x = 0
    while x < len(cells):
        y = 0
        while y < len(cells[0]):
            if cells[x][y] == "^":
                cells[x][y] = "."
                return [x,y]
            y += 1
        x += 1

direction = 0 # 0-up 1-down 2-right 3-left
x,y = findStart()
visited = set()
while not ((direction == 0 and x == 0) or (direction == 1 and x == len(cells)-1) or (direction == 2 and y == len(cells[0])-1) or (direction == 3 and y == 0)):
    visited.add(x*1000000+y)
    if direction == 0:
        if cells[x-1][y] in ["."]:
            x -= 1
        else:
            direction = 2
    elif direction == 1:
        if cells[x+1][y] in ["."]:
           x += 1
        else:
            direction = 3
    elif direction == 2:
        if cells[x][y+1] in ["."]:
            y += 1
        else:
            direction = 1
    elif direction == 3:
        if cells[x][y-1] in ["."]:
            y -= 1
        else:
            direction = 0
print("Answer is: ", len(visited)+1)