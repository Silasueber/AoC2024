content = [line.strip() for line in open("./data.txt", "r").readlines()]
content = [list(l) for l in content]


count = 0
visited = []
cluster = []
for i in range(len(content)):
    for j in range(len(content[0])):
        if [i,j] not in visited:
            stack = [[i,j]]
            clusterPermitter = 0
            currentCluster = []
            while len(stack) > 0:
                x,y = stack.pop()
                currentCluster.append([x,y])
                visited.append([x,y])
                if x > 0 and content[x-1][y] == content[x][y] and [x-1,y] not in visited and [x-1,y] not in stack:
                    stack.append([x-1,y])
                if y > 0 and content[x][y-1] == content[x][y] and [x,y-1] not in visited and [x,y-1] not in stack:
                    stack.append([x,y-1])
                if x < len(content)-1 and content[x+1][y] == content[x][y] and [x+1,y] not in visited and [x+1,y] not in stack:
                    stack.append([x+1,y])
                if y < len(content[0])-1 and content[x][y+1] == content[x][y] and [x,y+1] not in visited and [x,y+1] not in stack:
                    stack.append([x,y+1])
            cluster.append(currentCluster)





count = 0
for c in cluster:
    same = 0
    print(c)
    for l in c:
        x,y = l
        left = y == 0 or content[x][y-1] != content[x][y]
        right = y == len(content[0])-1 or content[x][y+1] != content[x][y]
        up = x == 0 or content[x-1][y] != content[x][y]
        down = x == len(content)-1 or content[x][y] != content[x+1][y]

        topLeft = y > 0 and x > 0 and content[x][y] != content[x-1][y-1]
        topRight = x > 0 and y < len(content[0])-1 and content[x][y] != content[x-1][y+1]
        bottomLeft = y > 0 and x < len(content)-1 and content[x][y] != content[x+1][y-1]
        bottomRight = y < len(content[0])-1 and x < len(content)-1 and content[x][y] != content[x+1][y+1]


        
        #case 1
        if left and up:
            same += 1
        if left and down:
            same += 1
        if right and up:
            same += 1
        if right and down:
            same += 1

        if not up and not left and topLeft:
            same += 1
        if not up and not right and topRight:
            same += 1
        if not down and not left and bottomLeft:
            same += 1
        if not down and not right and bottomRight:
            same += 1
    count += same*len(c)
        
    print(same)
print(count)