content = [list(int(t) for t in line.strip()) for line in open("./example.txt", "r").readlines()][0]

line = []
for i in range(len(content)):
    if content[i] > 0:
        if i%2 == 0:
            line.append([str(i//2)]*content[i])
        else:
            line.append(["."]*content[i])

i = len(line)-1
while line[i][0] == ".":
    i -= 1

for x in range(0,len(line)):

    found = False
    if i == ".":
        i -= 1
        break
    for l in range(i):
        if found:
            break
        if line[l][0] == "." and len(line[l]) >= len(line[i]) and not found:
            len_high = len(line[i])
            diff = len(line[l]) - len(line[i])
            high_pop = line.pop(i)
            i-=1
            low_pop = line.pop(l)
            i-=1
            line.insert(l,high_pop)
            i+=1
            if len(high_pop) != len(low_pop):
                line.insert(l+1,["."]*(diff))
                line.insert(i+1,["."]*(len_high))
            else:
                line.insert(i,["."]*(len_high))

            found = True
            
           
l = []
for i in line:
    for x in i:
        l.append(x)
print(l)        
count = 0
for i in range(len(l)):
    if l[i] != ".":
        count += i*int(l[i])
print("Answer is: ", count)
#print("Answer is: ", count)
