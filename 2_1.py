with open("data/2.txt", "r") as file:
    safe = 0
    for line in file:

        mylist = [int(i) for i in line.split()]
        
        print(mylist)

        decreasing = all([mylist[i] < mylist[i+1] for i in range(len(mylist)-1)])
        increasing = all([mylist[i] > mylist[i+1] for i in range(len(mylist)-1)])
        enough_distance = all([abs(mylist[i] - mylist[i+1]) <= 3 for i in range(len(mylist)-1)])
        not_enough_distance = all([abs(mylist[i] - mylist[i+1]) >= 1 for i in range(len(mylist)-1)])

        print(decreasing, increasing, enough_distance, not_enough_distance)
        if (decreasing or increasing) and enough_distance and not_enough_distance:
            print("safe", mylist)
            safe += 1
            continue

print(safe)
