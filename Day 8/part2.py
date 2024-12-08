content = [list(line.strip()) for line in open("./data.txt", "r").readlines()]

antenna_map = {}
for x in range(len(content)):
    for y in range(len(content[0])):
        if content[x][y] != ".":
            if content[x][y] in antenna_map: 
                antenna_map[content[x][y]] += [[x,y]]
            else:
                antenna_map[content[x][y]] = [[x,y]]

nodes = set()
for key in antenna_map:
    for i in range(len(antenna_map[key])):
        for x in range(i+1,len(antenna_map[key])):
            left = antenna_map[key][i]
            right = antenna_map[key][x]
            nodes.add((left[0])*10000+left[1])
            nodes.add((right[0])*10000+right[1])
            diff_x, diff_y = left[0]-right[0], left[1]-right[1]
            try:
                while left[0]+diff_x >= 0 and left[1]+diff_y >= 0:
                    content[left[0]+diff_x][left[1]+diff_y] = "#"
                    nodes.add((left[0]+diff_x)*10000+left[1]+diff_y)
                    left = [left[0]+diff_x,left[1]+diff_y]
            except:
                print("Outside")
            try:
                while right[0]-diff_x >= 0 and right[1]-diff_y >= 0:
                    content[right[0]-diff_x][right[1]-diff_y] = "#"
                    nodes.add((right[0]-diff_x)*10000+right[1]-diff_y)
                    right = [right[0]-diff_x,right[1]-diff_y]
            except:
                print("Outside")
print(nodes)          
for i in content:
    print("".join(i))
print("Answer is: ", len(nodes))

