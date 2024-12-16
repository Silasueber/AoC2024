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
    moves += list(moves[0])

for move in moves:
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
    elif newField == "O":
        checker = [pos[0]+direction[0],pos[1]+direction[1]]
        # check in move direction if there is free
        while content[checker[0]][checker[1]] == "O":
            checker = [checker[0]+direction[0],checker[1]+direction[1]]
        if content[checker[0]][checker[1]] == ".":
            content[checker[0]][checker[1]] = "O"
            content[pos[0]+direction[0]][pos[1]+direction[1]] = "."
            pos = [pos[0]+direction[0],pos[1]+direction[1]]

gps = 0
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == "O":
            gps += i*100+j
    print(content[i])
print(gps)