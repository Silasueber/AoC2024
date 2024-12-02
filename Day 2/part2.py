file = open("./data.txt", "r")
amount_safe = 0

while True:
    content=file.readline()
    if not content:
        break
    levels = content.split(" ")
    t = 0
    solved = False
    while t < len(levels):
        subArray = levels[0:t] + levels[t+1:len(levels)]
        i = 0
        last = None
        inc = True
        safe = True
        while i < len(subArray):
            if i == 0:
                last = int(subArray[i])
            elif i == 1:
                if  int(subArray[i]) < last:
                    inc = False
                if abs(last- int( int(subArray[i]))) >= 1 and abs(last- int(subArray[i])) <= 3:
                    last =  int(subArray[i])
                else:
                    safe = False
            else:
                if inc and  int(subArray[i]) > last:
                    if abs(last- int(subArray[i])) >= 1 and abs(last- int(subArray[i])) <= 3:
                        last =  int(subArray[i])
                    else:
                        safe = False
                elif not inc and  int(subArray[i]) < last:
                    if abs(last- int(subArray[i])) >= 1 and abs(last- int(subArray[i])) <= 3:
                        last =  int(subArray[i])
                    else:
                        safe = False
                else:
                    safe = False
            i+=1
        if safe:
            if not solved:
                amount_safe += 1   
                solved = True 
        t += 1
file.close()

print("Answer is: ", amount_safe)

