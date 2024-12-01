file = open("./data.txt", "r")

left = []
right = []

while True:
    content=file.readline()
    if not content:
        break
    content = content.split("   ")
    left.append(int(content[0]))
    right.append(int(content[1]))
file.close()


distance = 0
i = 0
while i < len(left):
    distance += left[i]*right.count(left[i])
    i += 1
print("Result: ", distance)

