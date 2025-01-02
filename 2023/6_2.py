import math
file = 'data/6_ex.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    for row in data.split("\n"):
       print(row)


    # couples = [(71530, 940200)]

    couples = [(35696887, 213116810861248)]

    total = 1
    for i in couples:
        # Polynom is: x(a-x)>b, so:  -x2 + ax - b  > 0
        delta = (i[0]**2 - 4*i[1])**0.5
        x1 = (i[0] - delta)/2
        x2 = (i[0] + delta)/2
        print(int(abs(math.ceil(x2)-math.floor(x1)-1)))
        total = total * int(abs(math.ceil(x2)-math.floor(x1)-1))

    print(total)