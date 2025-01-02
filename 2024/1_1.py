file = "data/1.txt"

with open(file, "r") as f:
    data = f.readlines()

leftcol = []
rightcol = []
for i in data:
    nb1, nb2 = i.split()
    leftcol.append(int(nb1))
    rightcol.append(int(nb2))

leftcol_sorted = sorted(leftcol)
rightcol_sorted = sorted(rightcol)

print(leftcol_sorted)
print(rightcol_sorted)


for i in range(len(leftcol_sorted)):
    print(abs(leftcol_sorted[i]-rightcol_sorted[i]))

print(sum([abs(leftcol_sorted[i]-rightcol_sorted[i]) for i in range(len(leftcol_sorted))]))
