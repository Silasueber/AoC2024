from scipy.optimize import linprog


content = [line.strip() for line in open("./data.txt", "r").readlines()]



obj = [3, 1] # 3 tokens for a and 1 for b


def solve(a,b,goal):
    lhs_eq = [[a[0],b[0]],[a[1],b[1]]]  # Green constraint left side
    rhs_eq = [goal[0],goal[1]]       # Green constraint right side
    bnd = [(0,float("inf")),(0,float("inf"))]
    opt = linprog(c=obj, A_ub=None, b_ub=None,
                A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
            method="revised simplex")
    return opt.x


# goal =[8400,5400]
# a = [94,34]
# b = [22,67]
# solve(a,b,goal)

# goal =[12784,12176]
# a = [26,66]
# b = [67,21]
# solve(a,b,goal)

# goal =[7870,6450]
# a = [17,86]
# b = [84,37]
# solve(a,b,goal)

# goal =[18641,10279]
# a = [69,23]
# b = [27,71]
# solve(a,b,goal)

count = 0
for i in range(len(content)):
    if i % 4 == 0:
        x,y = content[i].split(": ")[1].split(", ")
        a = [int(x.split("+")[1]),int(y.split("+")[1])]
    elif i % 4 == 1:
        x,y = content[i].split(": ")[1].split(", ")
        b = [int(x.split("+")[1]),int(y.split("+")[1])]
    elif i % 4 == 2:
        x,y = content[i].split(": ")[1].split(", ")
        goal = [int(x.split("=")[1]),int(y.split("=")[1])]
    else:
        # print(a,b,goal)
        result = solve(a,b,goal)
        if result[0]%1 < 0.00001 and result[1]%1 < 0.00001:
            count += round(result[0])*3+round(result[1])

result = solve(a,b,goal)
if result[0]%1 < 0.00001 and result[1]%1 < 0.00001:
    count += round(result[0])*3+round(result[1])
print(count)



