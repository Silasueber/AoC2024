rules = open("./data.txt", "r")
prints = open("./data2.txt", "r")

ruleList = {}
while True:
    content=rules.readline()
    if not content:
        break
    left, right = content.split("|")
    if int(left) not in ruleList:
        ruleList[int(left)] = [int(right)]
    else:
        ruleList[int(left)].append(int(right))
rules.close()

count = 0
while True:
    content=prints.readline()
    if not content:
        break
    commands = content.split(",")
    i = 1
    error = False
    while i < len(commands) and not error:
        y = 0
        if int(commands[i]) in ruleList :
            while y < i:
                if int(commands[y]) in ruleList[int(commands[i])]:
                    error = True
                    break
                y += 1
        i += 1
    if not error:
        count += int(commands[int(len(commands)/2)])
        
prints.close()

print("Answer is: ", count)

