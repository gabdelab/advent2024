def safe(mylist):
    decreasing = all([mylist[i] < mylist[i+1] for i in range(len(mylist)-1)])
    increasing = all([mylist[i] > mylist[i+1] for i in range(len(mylist)-1)])
    enough_distance = all([abs(mylist[i] - mylist[i+1]) <= 3 for i in range(len(mylist)-1)])
    not_enough_distance = all([abs(mylist[i] - mylist[i+1]) >= 1 for i in range(len(mylist)-1)])
    return (decreasing or increasing) and enough_distance and not_enough_distance

with open("data/2.txt", "r") as file:
    is_safe = 0
    for line in file:

        mylist = [int(i) for i in line.split()]
        
        if safe(mylist):
            is_safe += 1
            continue

        print(mylist)
        for j in range(len(mylist)):
            
            mylist2 = mylist[:j] + mylist[j+1:]
            if safe(mylist2):
                print("safe: ", mylist2)
                is_safe += 1
                break

    

print(is_safe)
