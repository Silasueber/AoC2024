# file = open("./example.txt", "r")

# letters = []
# count = 0

# while True:
#     content=file.readline()
#     if not content:
#         break
#     if content.find('\n') != -1:
#         l = list(content)
#         l.remove("\n")
#         letters.append(l)
#     else:
#         letters.append(list(content))
# file.close()

# XMAS = ["X","M","A","S"]
# def depthSearch(x,y,letter):
#     global count
#     print(letter)
#     if letters[x][y] == "S":
#         print("found", letter)
#         count += 1 
#     else:
#         if x < len(letters)-1 and y > 0 and letters[x+1][y-1] == XMAS[letter]:
#             depthSearch(x+1,y-1,letter+1)
#         if x < len(letters)-1 and letters[x+1][y] == XMAS[letter]:
#             depthSearch(x+1,y,letter+1)
#         if x < len(letters)-1 and y < len(letters[0])-1 and letters[x+1][y+1] == XMAS[letter]:
#             depthSearch(x+1,y+1,letter+1)
#         if x > 0 and y > 0 and letters[x-1][y-1] == XMAS[letter]:
#             depthSearch(x-1,y-1,letter+1)
#         if x > 0 and letters[x-1][y] == XMAS[letter]:
#             depthSearch(x-1,y,letter+1)
#         if x > 0 and y < len(letters[0])-1 and letters[x-1][y+1] == XMAS[letter]:
#             depthSearch(x-1,y+1,letter+1)
#         if y > 0 and letters[x][y-1] == XMAS[letter]:
#             depthSearch(x,y-1,letter+1)
#         if y < len(letters[0])-1 and letters[x][y+1] == XMAS[letter]:
#             depthSearch(x,y+1,letter+1)

# x = 0
# while x < len(letters):
#     y = 0
#     while y < len(letters[0]):
#         if letters[x][y] == XMAS[0]:
#             depthSearch(x,y,1)
#         y += 1
#     x += 1



# print("Answer is: ", count)

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

def depthSearch(x,y):
    global count
    if x < len(letters)-3 and y-3 >= 0 and letters[x+1][y-1] == "M" and letters[x+2][y-2] == "A" and letters[x+3][y-3] == "S":
        count += 1
    if x < len(letters)-3 and letters[x+1][y] == "M" and letters[x+2][y] == "A" and letters[x+3][y] == "S":
        count += 1
    if x < len(letters)-3 and y < len(letters[0])-3 and letters[x+1][y+1] == "M" and letters[x+2][y+2] == "A" and letters[x+3][y+3] == "S":
        count += 1
    if x-3 >= 0 and y-3 >= 0 and letters[x-1][y-1] ==  "M" and letters[x-2][y-2] == "A" and letters[x-3][y-3] == "S":
        count += 1
    if  x-3 >= 0 and letters[x-1][y] ==  "M" and letters[x-2][y] == "A" and letters[x-3][y] == "S":
       count += 1
    if  x-3 >= 0 and y < len(letters[0])-3 and letters[x-1][y+1] =="M" and letters[x-2][y+2] == "A" and letters[x-3][y+3] == "S":
        count += 1
    if y-3 >= 0 and letters[x][y-1] ==  "M" and letters[x][y-2] == "A" and letters[x][y-3] == "S":
        count += 1
    if y < len(letters[0])-3 and letters[x][y+1] == "M" and letters[x][y+2] == "A" and letters[x][y+3] == "S":
       count += 1

x = 0
while x < len(letters):
    y = 0
    while y < len(letters[0]):
        if letters[x][y] == "X":
            depthSearch(x,y)
        y += 1
    x += 1



print("Answer is: ", count)

