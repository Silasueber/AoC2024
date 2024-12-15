import numpy as np
from PIL import Image

content = [line.strip() for line in open("./data.txt", "r").readlines()]
example = False
if example:
    limitX = 7
    limitY = 11
else:
    limitX = 103
    limitY = 101

quads = {}
# Solution 6620
# for steps in range(5000,10500):
#     end = []
#     for c in content:
#         xs, ys = c.split(" ")[0].split("=")[1].split(",")
#         xv, yv = c.split(" ")[1].split("=")[1].split(",")
#         xs = int(xs)
#         ys = int(ys)
#         xv = int(xv)
#         yv = int(yv)
#         finalX = (xs + xv * steps) % limitY
#         finalY = (ys + yv * steps) % limitX
#         end.append([finalX,finalY])



#     quadrant = [0,0,0,0]

#     im = []
#     for i in range(limitX):
        
#         line = []
#         for j in range(limitY):
#             line.append(end.count([j,i])*255)
#         im.append(line)
#     a = np.array(im, np.uint8)
#     print(a)

#     Image.fromarray(a).save("./images/"+str(steps)+".png")
#     print("---------------------"+str(steps)+"---------------------------------")


end = []
for c in content:
    xs, ys = c.split(" ")[0].split("=")[1].split(",")
    xv, yv = c.split(" ")[1].split("=")[1].split(",")
    xs = int(xs)
    ys = int(ys)
    xv = int(xv)
    yv = int(yv)
    finalX = (xs + xv * 6620) % limitY
    finalY = (ys + yv * 6620) % limitX
    end.append([finalX,finalY])

for i in range(limitX):
    line = ""
    for j in range(limitY):
        if [j,i] in end:
            line += str(end.count([j,i]))
        else:
            line += "."
    print(line)

