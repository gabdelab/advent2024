file = 'data/12.txt'

precomputed = {}
NB_PRECOMPUTED = 0
NB_COMPUTED = 0

def compute(word, expectations):
    global NB_COMPUTED, NB_PRECOMPUTED
    # print(word, expectations)
    # First get in precomputed
    if precomputed.get(word+str(expectations), None) is not None:
        NB_PRECOMPUTED += 1
        return precomputed[word+str(expectations)]
    NB_COMPUTED = NB_COMPUTED + 1
    nb_hash = word.count("#")
    nb_dot = word.count(".")
    nb_question = word.count("?")

    if not expectations and nb_hash > 0:
        return 0

    if word == "":
        if expectations:
            toreturn = 0
            precomputed[word+str(expectations)] = toreturn
            return toreturn
        toreturn = 1
        precomputed[word+str(expectations)] = toreturn
        return toreturn

    if len(expectations) == 1 and len(word) == expectations[0] and nb_dot == 0:
        toreturn = 1
        precomputed[word+str(expectations)] = toreturn
        return toreturn

    if len(word) < sum(expectations) + len(expectations) - 1:
        toreturn = 0
        precomputed[word+str(expectations)] = toreturn
        return toreturn

    if word[0] == ".":
        toreturn = compute(word[1:], expectations)
        precomputed[word+str(expectations)] = toreturn
        return toreturn


    if word[0] == "?":
        toreturn = compute(word[1:], expectations) + compute("#"+word[1:], expectations)
        precomputed[word+str(expectations)] = toreturn
        return toreturn

    if word[0] == "#":
        # Exit condition 1: a dot before expectations[0]
        if word.find(".") > -1 and word.find(".") < expectations[0]:
            toreturn = 0
            precomputed[word+str(expectations)] = toreturn
            return toreturn
        # Exit condition 2: a hash on expectations[0] + 1
        if word[expectations[0]] == "#":
            toreturn = 0
            precomputed[word+str(expectations)] = toreturn
            return toreturn
        toreturn = compute(word[expectations[0]+1:], expectations[1:])
        precomputed[word+str(expectations)] = toreturn
        return toreturn


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    total = 0
    for row in data.split("\n"):
        NB_PRECOMPUTED = 0
        NB_COMPUTED = 0
        chars, data = row.split(" ")
        chars = chars+"?"+chars+"?"+chars+"?"+chars+"?"+chars
        data = data + "," + data + "," + data + "," + data + "," + data 
        expectations = [int(i) for i in data.split(",")]

        subtotal = compute(chars, expectations)
        print(row, " - precomputed:", NB_PRECOMPUTED, ", recomputed:", NB_COMPUTED)
        total += subtotal
    print(len(precomputed.keys()))
    print(total)