content = [line.strip() for line in open("./example.txt", "r").readlines()]
content = [list(l) for l in content]


# cluster = []

# visited = []
# for i in range(len(content)):
#     for j in range(len(content[0])):
#         if [i,j] not in visited:
#             stack = [[i,j]]
#             while len(stack) > 0:
#                 x,y = stack.pop()
#                 visited.append([x,y])
#                 print(x,y)
#                 if x > 0 and content[x-1][y] == content[x][y] and [x-1,y] not in visited:
#                     stack.append([x-1,y])
#                 if y > 0 and content[x][y-1] == content[x][y] and [x,y-1] not in visited:
#                     stack.append([x,y-1])
#                 if x < len(content)-1 and content[x+1][y] == content[x][y] and [x+1,y] not in visited:
#                     stack.append([x+1,y])
#                 if y < len(content[0])-1 and content[x][y+1] == content[x][y] and [x,y+1] not in visited:
#                     stack.append([x,y+1])
#             cluster.append(visited)
# print(cluster)

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
                elif [x-1,y] not in currentCluster and [x-1,y] not in stack:
                    
                    clusterPermitter += 1

                if y > 0 and content[x][y-1] == content[x][y] and [x,y-1] not in visited and [x,y-1] not in stack:
                    stack.append([x,y-1])
                elif [x,y-1] not in currentCluster and [x,y-1] not in stack:
                    
                    clusterPermitter += 1

                if x < len(content)-1 and content[x+1][y] == content[x][y] and [x+1,y] not in visited and [x+1,y] not in stack:
                    stack.append([x+1,y])
                elif [x+1,y] not in currentCluster and [x+1,y] not in stack:
                  
                    clusterPermitter += 1

                if y < len(content[0])-1 and content[x][y+1] == content[x][y] and [x,y+1] not in visited and [x,y+1] not in stack:
                    stack.append([x,y+1])
                elif [x,y+1] not in currentCluster and [x,y+1] not in stack:
                   
                    clusterPermitter += 1
            count += len(currentCluster) * clusterPermitter
            cluster.append(currentCluster)

print(cluster)
print("Answer is: ", count)

