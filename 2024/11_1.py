def decide(mylist, occurences):
    if occurences == 0:
        return len(mylist)
    if mylist == []:
        return 0
    if mylist[0] == 0:
        out = [1]
    elif len(str(mylist[0])) % 2 == 0:
        out = [int(str(mylist[0])[:len(str(mylist[0]))//2]), 
               int(str(mylist[0])[len(str(mylist[0]))//2:])]
    else:
        out = [mylist[0] * 2024]
    first_item = decide(out, occurences - 1)
    return first_item + decide(mylist[1:], occurences)

data = []
with open("data/11_ex.txt", "r") as file:
    for line in file.read().split(" "):
        data.append(int(line.strip()))
print(decide(data, 25))