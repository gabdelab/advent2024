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

out = []
read_index = 0
while read_index < len(program):

    instruction = program[read_index]
    operand = program[read_index+1]
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
        print(new_output, registerA, registerB, registerC, operand, instruction, read_index)
        out.append(new_output)
    elif instruction == 6:
        registerB = int(registerA/(2**get_combo_operand(registerA, registerB, registerC, operand)))
    elif instruction == 7:
        registerC = int(registerA/(2**get_combo_operand(registerA, registerB, registerC, operand)))
    read_index += 2

print("out", ",".join([str(i) for i in out]), "registers", registerA, registerB, registerC)