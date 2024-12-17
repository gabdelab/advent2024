import re
import time
data = []

regex = re.compile(r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.*)")
with open("data/17.txt", "r") as file:
    wd = regex.match(file.read())
    registerA = int(wd.groups()[0])
    registerB = int(wd.groups()[1])
    registerC = int(wd.groups()[2])
    program = [int(i) for i in wd.groups()[3].split(",")]

print(registerA, registerB, registerC, program)

def get_combo_operand(registerA, registerB, registerC, instruction):
    if instruction < 4:
        return instruction
    if instruction == 4:
        return registerA
    if instruction == 5:
        return registerB
    if instruction == 6:
        return registerC
    if instruction == 7:
        raise ValueError(f"Invalid instruction {instruction}")
original_registerA = registerA
original_registerB = registerB
original_registerC = registerC

for orig in range(10000000000000):
    orig *= 1073741824
    additional = [520436751, 522009615, 524106767, 528301071, 896547855, 896613391, 896699313, 896744463, 900742159, 900807695, 900938767]
    # additional = [1063951, 1129487, 1215409, 1260559, 1653775, 1195023, 343055, 1915919]
    for j in additional:
        i = orig + j
        registerA = i
        registerB = original_registerB
        registerC = original_registerC
        out = []
        read_index = 0
        impossible = False
        pointer = 0
        while read_index < len(program) and not impossible:
            if len(out) > len(program):
                impossible = True
                continue
            instruction = program[read_index]
            operand = program[read_index+1]
            # print(read_index, instruction, operand, registerA, registerB, registerC)
            if instruction == 0:
                registerA = int(registerA/(2**get_combo_operand(registerA, registerB, registerC, operand)))
            elif instruction == 1:
                registerB = registerB ^ operand
            elif instruction == 2:
                registerB = get_combo_operand(registerA, registerB, registerC, operand) % 8
            elif instruction == 3:
                if registerA != 0:
                    read_index = operand
                    continue
            elif instruction == 4:
                registerB = registerB ^ registerC
            elif instruction == 5:
                new_output = get_combo_operand(registerA, registerB, registerC, operand) % 8
                out.append(new_output)
                if new_output != program[pointer]:
                    impossible = True
                    continue
                else:
                    if len(out) > 15:
                        print(out, registerA, i)            
                pointer += 1
            elif instruction == 6:
                registerB = int(registerA/(2**get_combo_operand(registerA, registerB, registerC, operand)))
            elif instruction == 7:
                registerC = int(registerA/(2**get_combo_operand(registerA, registerB, registerC, operand)))
            read_index += 2
        if out == program:
            print("found", i)
            break
print("out", ",".join([str(i) for i in out]), "registers", registerA, registerB, registerC)