import re 
file = open("./data.txt", "r")
content=file.readline()
count = 0
positions = [[m.start(0), m.end(0)] for m in re.finditer("mul\([0-9]*,[0-9]*\)", content)]
last = 0
calc = True
for t in positions:
    print(content[last:t[1]])
    dos = [[m.start(0), m.end(0)] for m in re.finditer("don't|do", content[last:t[1]])]
    left, right = content[t[0]+4:t[1]].split(")")[0].split(",")
    if len(dos) != 0:
        if dos[-1][1]-dos[-1][0] == 5:
            calc = False
        else:
            calc = True
    if calc:
        count += int(left) * int(right)
    last = t[1]
file.close()
print("Answer is: ", count)