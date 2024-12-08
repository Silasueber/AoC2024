from datetime import datetime
startTime = datetime.now()

content = [line.strip() for line in open("./data.txt", "r").readlines()]

count = 0
for l in content:
    result, numbers = l.split(": ")
    numbers = [int(n) for n in numbers.split(" ")]
    result = int(result)
    for i in range(2**(len(numbers)-1)):
        operations = format(i, '0{0}b'.format(len(numbers)-1))
        value = numbers[0]
        for t in range(len(numbers)-1):
            if operations[t] == "0":
                value += numbers[t+1]
            else:
                value *= numbers[t+1]
        if value == result:
            count += result
            break



print("Answer is: ", count)
print("Took: ", datetime.now() - startTime)

