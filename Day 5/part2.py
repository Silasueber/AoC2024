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

errors = []
while True:
    content=prints.readline()
    if not content:
        break
    commands = [int(x) for x in content.split(",")]
    i = 1
    error = False
    while i < len(commands) and not error:
        y = 0
        if commands[i] in ruleList:
            while y < i:
                if commands[y] in ruleList[commands[i]]:
                    error = True
                    errors.append(commands)
                    break
                y += 1
        i += 1
prints.close()

count = 0
for e in errors:
    i = 1
    while i < len(e):
            y = 0
            if e[i] in ruleList:
                while y < i:
                    if e[y] in ruleList[e[i]]:
                        e = e[0:y] + [e[i]] + e[y:i] + e[i+1:]
                        break
                    y += 1
            i += 1
    print(e)
    count += e[int(len(e)/2)]

print("Answer is: ", count)

