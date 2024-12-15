content = [line.strip().split(" ") for line in open("./data.txt", "r").readlines()]
counter = 0
for c in content:
    c = [int(l) for l in c]
    t = c.copy()
    t.sort()
    b = c.copy()
    b.sort(reverse = True)
    error = False
    if t == c or c == b:
        for i in range(1,len(c)):
            if abs(int(c[i])-int(c[i-1])) < 1 or abs(int(c[i])-int(c[i-1])) > 3:
                error = True
        if not error:
            counter += 1
        else:
            print(c)
print(counter)