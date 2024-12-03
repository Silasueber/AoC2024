import re 

file = open("./data.txt", "r")

content=file.readline()
x = re.findall("mul\([0-9]*,[0-9]*\)",content)
i = 0
count = 0
print(x)
while i < len(x):
    left, right = x[i][4:].split(")")[0].split(",")
    print(left,right)
    count += int(left) * int(right)
    i += 1
file.close()

print("Answer is: ", count)

