a = 4

output = -1

steps = [2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0]
counter = 8**(len(steps)-1)
for x in range(len(steps)-1,-1,-1):
    for i in range(counter,counter+8**(x+1),8**(x)):
        a = i
        b = 0
        c = 0
        o = []
        for _ in range(x+1):
            b = a % 8
            # print(b)
            b = b ^ 1
            #print(b)
            c = int(a/(2**b))
            #print(a,c)
            # print(c)
            b = b ^ 5
            #print(b)
            b = b ^ c
            #print(b)
            a = int(a/8)
            #print(a)
            o.append(b%8)
        print(i, o, b%8)
        if b%8 == steps[x]:
            counter = i
            print("FOUND", i)
            break

for i in range(164540892147351,164540892147451):
    a = i
    b = 0
    c = 0
    o = []
    
    b = a % 8
    # print(b)
    b = b ^ 1
    #print(b)
    c = int(a/(2**b))
    #print(a,c)
    # print(c)
    b = b ^ 5
    #print(b)
    b = b ^ c
    #print(b)
    a = int(a/8)
    #print(a)
    o.append(b%8)
    if b%8 == 2:
        counter = i
        print("FOUND", i)
# 140737488355328
# 30786325577728