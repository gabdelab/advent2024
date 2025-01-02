file = "data/1.txt"


with open(file, "r") as f:
    data = f.readlines()

leftcol = []
rightcol = {}
for i in data:
    nb1, nb2 = i.split()
    leftcol.append(int(nb1))
    try:
        rightcol[int(nb2)] += 1
    except:
        rightcol[int(nb2)] = 1

print(rightcol)
total = 0
for i in leftcol:
    try:
        total += rightcol[i] * i 
    except:
        total += 0

print(total)