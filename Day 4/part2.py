
file = open("./data.txt", "r")

letters = []
count = 0

while True:
    content=file.readline()
    if not content:
        break
    if content.find('\n') != -1:
        l = list(content)
        l.remove("\n")
        letters.append(l)
    else:
        letters.append(list(content))
file.close()

x = 0
while x < len(letters):
    y = 0
    while y < len(letters[0]):
        if x > 0 and y > 0 and x < len(letters)-1 and y < len(letters[0])-1 and letters[x][y] == "A" and ((letters[x-1][y-1] == "M" and letters[x+1][y+1] == "S") or (letters[x-1][y-1] == "S" and letters[x+1][y+1] == "M")) and ((letters[x-1][y+1] == "M" and letters[x+1][y-1] == "S") or (letters[x-1][y+1] == "S" and letters[x+1][y-1] == "M")):
            print("Found")
            count += 1
        y += 1
    x += 1



print("Answer is: ", count)

