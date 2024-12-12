content = [line.strip().split(" ") for line in open("./data.txt", "r").readlines()][0]
content = [int(x) for x  in content]
blink = {}
for n in content:
    if n in blink:
        blink[n] += 1
    else:
        blink[n] = 1
for i in range(75):
    top = {}
    for number in blink:
        if number == 0:
            if 1 in top:
                top[1] += blink[number]
            else:
                top[1] = blink[number]
        elif len(str(number))%2 == 0:
            left = int(str(number)[:len(str(number))//2])
            right = int(str(number)[len(str(number))//2:])
            if left in top:
                top[left] += blink[number]
            else:
                top[left] = blink[number]
            if right in top:
                top[right] += blink[number]
            else:
                top[right] = blink[number]
        else:
            newValue = number*2024
            if newValue in top:
                top[newValue] += blink[number]
            else:
                top[newValue] = blink[number]
    blink = top
count = 0
for t in blink:
    count += blink[t]
print("Answer is: ", count)

