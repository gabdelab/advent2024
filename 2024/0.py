data = []
with open("data/0.txt", "r") as file:
    for line in file:
        data.append(line.strip())
print(data)