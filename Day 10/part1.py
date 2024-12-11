content = [line.strip() for line in open("./data.txt", "r").readlines()]
content = [list(c) for c in content]

start = []
for x in range(len(content)):
    for y in range(len(content[0])):
        if content[x][y] == "0":
            start.append([x,y])

count = 0
for s in start:
    stack = [s]
    found = []
    while len(stack) > 0:
        x,y = stack.pop(0)
        if content[x][y] == "9" and [x,y] not in found:
            count +=1
            found.append([x,y])
        if x > 0 and int(content[x-1][y])-int(content[x][y]) == 1:
            stack.append([x-1,y])
        if y > 0 and int(content[x][y-1])-int(content[x][y]) == 1:
            stack.append([x,y-1])
        if x < len(content)-1 and int(content[x+1][y])-int(content[x][y]) == 1:
            stack.append([x+1,y])
        if y < len(content[0])-1 and int(content[x][y+1])-int(content[x][y]) == 1:
            stack.append([x,y+1])
print(count)


#print("Answer is: ", 0)

