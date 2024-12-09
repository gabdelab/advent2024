with open("data/9.txt", "r") as file:
    for line in file:
        data = line.strip()


current = 0
out = []
is_space = False
for i in data:
    if not is_space:
        sublist = [str(current) for _ in range(int(i))]
        out.extend(sublist)
        current += 1
    else:
        sublist = [" " for _ in range(int(i))]
        out.extend(sublist)
    is_space = not is_space
print(out)
while True:
    try:
        index = out.index(" ")
    except ValueError:
        break
    print(index)
    out[index] = out[-1]
    out = out[:-1]


total = sum(i_coord * int(i) for i_coord, i in enumerate(out))
print(total)
# print("computed out", out)
# print("expected out",  "0099811188827773336446555566")
