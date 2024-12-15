file = open("./data.txt", "r")


amount_safe = 0
while True:
    content=file.readline()
    if not content:
        break
    levels = content.split(" ")
    i = 0
    last = None
    inc = True
    safe = True
    while i < len(levels):
        if i == 0:
            last = int(levels[i])
        elif i == 1:
            if  int(levels[i]) < last:
                inc = False
            if abs(last- int(int(levels[i]))) >= 1 and abs(last- int(levels[i])) <= 3:
                last =  int(levels[i])
            else:
                safe = False
        else:
            if inc and  int(levels[i]) > last:
                if abs(last- int(levels[i])) >= 1 and abs(last- int(levels[i])) <= 3:
                    last =  int(levels[i])
                else:
                    safe = False
            elif not inc and  int(levels[i]) < last:
                if abs(last- int(levels[i])) >= 1 and abs(last- int(levels[i])) <= 3:
                    last =  int(levels[i])
                else:
                    safe = False
            else:
                safe = False
        i+=1
    if safe:
        print(levels)
        amount_safe += 1
file.close()

print("Answer is: ", amount_safe)

