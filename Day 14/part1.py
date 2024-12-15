import math
content = [line.strip() for line in open("./data.txt", "r").readlines()]
example = False
if example:
    limitX = 7
    limitY = 11
else:
    limitX = 103
    limitY = 101

end = []
for c in content:
    xs, ys = c.split(" ")[0].split("=")[1].split(",")
    xv, yv = c.split(" ")[1].split("=")[1].split(",")
    xs = int(xs)
    ys = int(ys)
    xv = int(xv)
    yv = int(yv)
    finalX = (xs + xv * 100) % limitY
    finalY = (ys + yv * 100) % limitX
    end.append([finalX,finalY])



quadrant = [0,0,0,0]
for i in range(limitX):
    line = ""
    for j in range(limitY):
        if [j,i] in end:
            line += str(end.count([j,i]))
            if j < limitY//2:
                if i < limitX//2:
                    quadrant[0] += end.count([j,i])
                elif i > limitX//2:
                    quadrant[1] += end.count([j,i])
            elif j > limitY//2:
                if i < limitX//2:
                    quadrant[2] += end.count([j,i])
                elif i > limitX//2:
                    quadrant[3] += end.count([j,i])

        else:
            line += "."
    print(line)
print("Answer is: ", math.prod(quadrant))

