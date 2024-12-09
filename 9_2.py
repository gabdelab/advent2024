with open("data/9.txt", "r") as file:
    for line in file:
        data = line.strip()

def clean_out(out, i):
    try:
        if out[i][0] == out[i+1][0]:
            out = out[:i] + [(out[i][0], out[i][1]+out[i+1][1])] + out[i+2:]
    except:
        return out
    return out

current = 0
out = []
is_space = False
files = []
for i in data:
    if not is_space:
        sublist = (str(current), int(i))
        out.append(sublist)
        files = [(str(current), int(i))] + files
        current += 1
    else:
        sublist = (" ", int(i))
        out.append(sublist)
    is_space = not is_space

for i in files:
    print(i)
    for index_elem, elem in enumerate(out):
        i_index = out.index(i)
        if index_elem > out.index(i):
            break
        if elem[0] == ' ':
            if elem[1] == i[1]:
                out[i_index] = (' ', i[1])
                out = clean_out(out, i_index)
                out = out[:index_elem] + [i] + out[index_elem+1:]
                break
            if elem[1] > i[1]:
                # Proceed to the replacement
                out[i_index] = (' ', i[1])
                out = clean_out(out, i_index)
                out = out[:index_elem] + [i, (' ', elem[1]-i[1])] + out[index_elem+1:]
                break
            else:
                continue
total = 0
counter = 0
for j, i in enumerate(out):
    if i[0] == ' ':
        counter += i[1]
        continue
    for yolo in range(i[1]):
        total += int(i[0])*counter
        counter += 1

print(total)