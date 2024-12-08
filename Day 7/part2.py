from datetime import datetime
startTime = datetime.now()


def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


content = [line.strip() for line in open("./data.txt", "r").readlines()]

currentRow = 0
count = 0
for l in content:
    currentRow += 1
    print(currentRow)
    result, numbers = l.split(": ")
    numbers = [int(n) for n in l.split(": ")[1].split(" ")]
    result = int(result)
    for i in range(3**(len(numbers)-1)):
        numbers = [int(n) for n in l.split(": ")[1].split(" ")]
        operations = ternary(i).zfill(len(numbers)-1)
        t = 0
        value = numbers.pop(0)
        while len(numbers) > 0:
            n = numbers.pop(0)
            if operations[t] == "0":
                value += n
            elif operations[t] == "1":
                value = value*10**(len(str(n)))+n
            else:
                value *= n
            t += 1
            if value > result:
                break
        if value == result:
            count += value
            break
            




print("Answer is: ", count)
print("Took: ", datetime.now() - startTime)

