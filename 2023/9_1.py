file = 'data/9.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()

    total = 0
    for row in data.split("\n"):
        if not row:
            continue
        suite = [int(i) for i in row.split(" ")]
        print(suite)

        mysuite = {0: suite}
        k = 0
        while any([i != 0 for i in mysuite[k]]):
            mysuite[k+1] = [mysuite[k][i+1]-mysuite[k][i] for i in range(len(mysuite[k])-1)]
            k += 1

        total += sum([j[-1] for j in mysuite.values()])
        print(mysuite)
    print(total)