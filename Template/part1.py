file = open("./data.txt", "r")


while True:
    content=file.readline()
    if not content:
        break
file.close()

print("Answer is: ", 0)

