content = [line.strip() for line in open("./data.txt", "r").readlines()]
count = 0
for i in range(len(content)+1):
    if i % 4 == 0:
        x,y = content[i].split(": ")[1].split(", ")
        a = [int(x.split("+")[1]),int(y.split("+")[1])]
    elif i % 4 == 1:
        x,y = content[i].split(": ")[1].split(", ")
        b = [int(x.split("+")[1]),int(y.split("+")[1])]
    elif i % 4 == 2:
        x,y = content[i].split(": ")[1].split(", ")
        goal = [int(x.split("=")[1]),int(y.split("=")[1])]
    else:
        A = (goal[0]*b[1]-goal[1]*b[0]) / (a[0]*b[1] - a[1]*b[0])
        B = (a[0]*goal[1]-a[1]*goal[0]) / (a[0]*b[1] - a[1]*b[0])
        if A.is_integer() and B.is_integer():
            if A > 100 or B > 100:
                print("TOO BIG")
            count += 3*A+B
print(count)