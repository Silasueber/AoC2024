import time 
start = time.time()


register_a = 164540892147389
register_b = 0
register_c = 0

steps = [2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0]

output = []

pointer = 0
while len(steps) > 1 and pointer < len(steps)-1:
    opcode = steps[pointer]
    operand = steps[pointer+1]
    if operand <= 3:
        combo_operand = operand
    elif operand == 4:
        combo_operand = register_a
    elif operand == 5:
        combo_operand = register_b
    elif operand == 6:
        combo_operand = register_c
    else:
        combo_operand = "NONE"

    if opcode == 0:
        numerator = register_a
        denominator = 2**combo_operand
        register_a = int(numerator/denominator)
        #print("adv", opcode, operand ,combo_operand)
    elif opcode == 1:
        register_b = register_b ^ operand
        #print("bxl", opcode, operand ,combo_operand)
    elif opcode == 2:
        register_b = combo_operand % 8
        #print("bst", opcode, operand ,combo_operand)
    elif opcode == 3:
        #print("jnz", opcode, operand ,combo_operand)
        if register_a != 0:
            pointer = operand
    elif opcode == 4:
        #print("bxc", opcode, operand ,combo_operand)
        register_b = register_b ^ register_c
    elif opcode == 5:
        #print("out", opcode, operand ,combo_operand)
        output.append(combo_operand%8)
    elif opcode == 6:
        #print("bdv", opcode, operand ,combo_operand)
        numerator = register_a
        denominator = 2**combo_operand
        register_b = int(numerator/denominator)
    elif opcode == 7:
        #print("cdv", opcode, operand ,combo_operand)
        numerator = register_a
        denominator = 2**combo_operand
        register_c = int(numerator/denominator)

    if not (opcode == 3 and register_a != 0):
        pointer += 2
        
print(output)


[2, 4, 1, 1, 7, 5, 1, 5, 4, 5, 0, 3, 5, 5, 3, 0]
[2, 4, 1, 1, 7, 5, 1, 5, 4, 5, 0, 3, 5, 5, 3, 0]