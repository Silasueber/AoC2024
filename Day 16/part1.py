content = [line.strip() for line in open("./data.txt", "r").readlines()]

start = [0,0]
end = [0,0]
for i in range(len(content)):
    content[i] = list(content[i])
    if "E" in content[i]:
        end = [i,content[i].index("E")]
    if "S" in content[i]:
        start = [i,content[i].index("S")]


bestWay = None
visited = {}
stack = [[start,0,1]] # up = 0 right = 1 down = 2 left = 3

while len(stack) > 0:
    pos = stack.pop(0)
    value = pos[1]
    facing = pos[2]
    pos = pos[0]
    if content[pos[0]][pos[1]] == "E":
        print(value)
        if bestWay == None:
            bestWay = value
        else:
            bestWay = min(bestWay,value)
    elif str(pos[0])+"X"+str(pos[1]) not in visited or visited[str(pos[0])+"X"+str(pos[1])] > value:
        visited[str(pos[0])+"X"+str(pos[1])] = value
        # UP
        if pos[0] > 0 and content[pos[0]-1][pos[1]] != "#":
            if facing == 0:
                stack.append([[pos[0]-1,pos[1]],value + 1, 0])
            else:
                stack.append([[pos[0]-1,pos[1]],value + 1001, 0])
        # DOWN
        if pos[0] < len(content)-1 and content[pos[0]+1][pos[1]] != "#":
            if facing == 2:
                stack.append([[pos[0]+1,pos[1]],value + 1, 2])
            else:
                stack.append([[pos[0]+1,pos[1]],value + 1001, 2])

        # LEFT
        if pos[1] > 0 and content[pos[0]][pos[1]-1] != "#":
            if facing == 3:
                stack.append([[pos[0],pos[1]-1],value +1,3])
            else:
                stack.append([[pos[0],pos[1]-1],value +1001,3])

        if pos[1] < len(content[0])-1 and content[pos[0]][pos[1]+1] != "#":
            if facing == 1:
                stack.append([[pos[0],pos[1]+1],value+1, 1])
            else:
                stack.append([[pos[0],pos[1]+1],value+1001, 1])


print(start,end)
print("Answer is: ", bestWay)

