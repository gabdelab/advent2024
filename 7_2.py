def is_doable(tosum, integers, leftover=None):
    if leftover and leftover > tosum:
        return False
    if tosum == leftover and integers == []:
        return True
    if integers == [] and tosum != leftover:
        return False
    via_sum = is_doable(tosum, integers[1:], (leftover or 0) + integers[0]) 
    via_mult = is_doable(tosum, integers[1:], (leftover or 1) * integers[0])
    via_concat = is_doable(tosum, integers[1:], int(str(leftover or "") + str(integers[0])))
    return via_sum or via_mult or via_concat

data = []
with open("data/7.txt", "r") as file:
    for line in file:
        tosum, integers = int(line.strip().split(":")[0]), [int(i) for i in line.strip().split(":")[1].strip().split(" ")]
        data.append((tosum, integers))

total = 0
for tosum, integers in data:
    if is_doable(tosum, integers):
        total += tosum
print(total)