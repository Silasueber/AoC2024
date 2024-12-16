content = [line.strip() for line in open("./maze.txt", "r").readlines()]
print(content)

print("Answer is: ", 0)

for i in range(len(content)):
    content[i] = list(content[i])
    for x in content[i]:
        if x == "@":
            pos = [i,content[i].index("@")]
            content[i][content[i].index("@")] = "."


m = [line.strip() for line in open("./instructions.txt", "r").readlines()]
moves = []
for i in m:
    moves += list(i)

# scale
newGrid = []
for i in range(len(content)):
    content[i] = list(content[i])
    ng = []
    for x in range(0,2*len(content[i])):
        if content[i][x//2] == "O":
            if x % 2== 0:
                ng.append("[")
            else:
                ng.append("]")
        else:
            ng.append(content[i][x//2])

    newGrid.append(ng)
pos = [pos[0],pos[1]*2]
for i in newGrid:
    print(i)

content = newGrid

visited = []
def checkBox(x,y, direction):
    global visited
    if [x,y] not in visited:
        
        if visited != "#":
            visited.append([x,y])
        if content[x][y] == ".":
            return True
        elif content[x][y] == "[":
            a = checkBox(x+direction,y,direction)
            b = checkBox(x,y+1,direction)
            return a & b
        elif content[x][y] == "]":
            a = checkBox(x+direction,y,direction)
            b = checkBox(x,y-1,direction)
            return a & b
        else:
            return False
    return True
          

for i in content:
    print(i)


for move in moves:
    print(move)
    print(pos)
   
    direction = []
    if move == "<":
        direction = [0,-1]
    elif move == ">":
        direction = [0,1]
    elif move == "^":
        direction = [-1,0]
    elif move == "v":
        direction = [1,0]
    newField = content[pos[0]+direction[0]][pos[1]+direction[1]]
    if newField == ".":
        pos = [pos[0]+direction[0],pos[1]+direction[1]]
    elif newField in ["[","]"] and direction[0] == 0: #left or right
        checker = [pos[0]+direction[0],pos[1]+direction[1]]
        while content[checker[0]][checker[1]] in ["[","]"]:
            checker = [checker[0]+direction[0],checker[1]+direction[1]]
        if content[checker[0]][checker[1]] == ".":
            if checker[1] > pos[1]: #move right
                content[checker[0]] = content[checker[0]][:pos[1]] + ["."] + content[checker[0]][pos[1]:checker[1]] + content[checker[0]][checker[1]+1:]
            else: # move left
                content[checker[0]] = content[checker[0]][:checker[1]]+content[checker[0]][checker[1]+1:pos[1]]+["."]+content[checker[0]][pos[1]:]
            pos = [pos[0]+direction[0],pos[1]+direction[1]]
    elif newField in ["[","]"]: #up or down
        visited = []
        a = checkBox(pos[0]+direction[0],pos[1],direction[0])
        if newField == "[":

            b = checkBox(pos[0]+direction[0],pos[1]+1,direction[0])
        else:
            b = checkBox(pos[0]+direction[0],pos[1]-1,direction[0])

        if a and b:
            newGrid = [row[:] for row in content]
            for i in visited:
                if direction[0] == -1:
                    if [i[0]+1,i[1]] in visited:
                        newGrid[i[0]][i[1]] = content[i[0]+1][i[1]]
                    else:
                        newGrid[i[0]][i[1]] = "."
                else:
                    if [i[0]-1,i[1]] in visited:
                        newGrid[i[0]][i[1]] = content[i[0]-1][i[1]]
                    else:
                        newGrid[i[0]][i[1]] = "."
            content = newGrid
            pos = [pos[0]+direction[0],pos[1]+direction[1]]
        print(visited)
    for i in content:
        print(i)

 
        

gps = 0
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == "[":
            gps += i*100+j
print(gps)