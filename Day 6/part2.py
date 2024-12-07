from datetime import datetime
startTime = datetime.now()
file = open("./data.txt", "r")
cells = [list(line.strip()) for line in file.readlines()]
file.close()
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


x,y = findStart()

def walk(x,y,cells, visited):
    direction = 0 # 0-up 1-down 2-right 3-left
    repeat = []
    while not ((direction == 0 and x == 0) or (direction == 1 and x == len(cells)-1) or (direction == 2 and y == len(cells[0])-1) or (direction == 3 and y == 0)):
        visited.add(x*1000+y)
        if [x,y,direction] in repeat:
            return True
        repeat.append([x,y,direction])
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
    visited.add(x*1000+y)
    return False
visited = set()
walk(x,y,cells, visited)
count = 0
for l in visited:
    new_x = int(l/1000)
    new_y = l%1000
    file = open("./data.txt", "r")
    cells = [list(line.strip()) for line in file.readlines()]
    file.close()
    if not (x == new_x and y == new_y):
        cells[new_x][new_y] = "#"
        cells[x][y] = "."
        v = set()
        if walk(x,y,cells,v):
            count+=1
print("Answer is: ", count)    
print("Took: ", datetime.now() - startTime)
