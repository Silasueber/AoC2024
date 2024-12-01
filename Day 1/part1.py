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

left.sort()
right.sort()

distance = 0
i = 0
while i < len(left):
    distance += abs(left[i]-right[i])
    i += 1
print("Answer is: ", distance)

