content = [list(int(t) for t in line.strip()) for line in open("./data.txt", "r").readlines()][0]

line = []
for i in range(len(content)):
    if i%2 == 0:
        line.append([str(i//2)]*content[i])
    else:
        line.append(["."]*content[i])

l = []
for i in line:
    for x in i:
        l.append(x)
low = 0
high = len(l)-1
while low < high:
    if l[low] != ".":
        low += 1
    elif l[high] == ".":
        high -= 1
    else:
        high_pop = l.pop(high)
        low_pop = l.pop(low)
        l.insert(low,high_pop)
        high -= 1
count = 0
for i in range(len(l)):
    if l[i] != ".":
        count += i*int(l[i])
print("Answer is: ", count)
