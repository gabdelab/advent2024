from itertools import combinations
from datetime import datetime as time
import re
file = 'data/12_2.txt'

def find_all(a_str, sub):
    results = []
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return results
        results.append(start)
        start += len(sub) # use start += 1 to find overlapping matches

def reduce(word, expectations):
    """
    Takes a word like ?#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#?
    and expectations like [1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6]
    to guess systematically what are the question marks
    """
    expectations = expectations.copy()
    if word and not expectations:
        return "." * len(word)
    if word == "":
        return ""
    if word[0] == ".":
        return "." + reduce(word[1:], expectations)
    # Find the first batch of contiguous # and ?
    end = word.find(".")
    first_hash = word[:end].find("#")
    contig_length = end if end > -1 else len(word)
    if first_hash == -1 or first_hash - 1 >= expectations[0]:
        # We exit here. nothing we can guess in this case
        return word

    if contig_length < expectations[0]:
        # We can't find the pattern here. We replace everything with .
        return "." * contig_length + reduce(word[end:], expectations)

    if contig_length > expectations[0] and first_hash not in [0,1]:
        # TODO we can do better here, ex. i have 10 areas of code and all can fit exactly in one place
        return word
    return "." * first_hash + "#" * expectations[0] + "." + reduce(word[expectations[0]+first_hash+1:], expectations[1:])


# reduce("?#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#?", [1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6])


def transform(word, expectations):
    """
        Make a bunch of decisions based on a word to ease later the number of possible permutations

        Remove all unplausible solutions

        ex.
        "???.###????.###????.###????.###????.###" with (1,1,3,1,1,3,1,1,3,1,1,3,1,1,3)

        - Since the max is 3 (5 times) and we observe 5 patterns of 3-length, we should replace ? with dots
            before and after these
    """
    max_expect = max(expectations)
    occurences = [i for i,j in enumerate(expectations) if j == max_expect]

    longest_char = len(word)
    found = False
    while longest_char >= max_expect:
        ifound = find_all(word, "#"*longest_char)
        if len(list(ifound))>0:
            break
        longest_char -= 1

    match_occurences = []
    if len(ifound) == len(occurences):
        for i in ifound:
            word = word[:max(i-1, 0)] + "." + word[i:i+longest_char] + "." + word[i+1+longest_char:]
        match_occurences.append([i, i+longest_char])


    # Optimization #2: If we haven't found the largest number, and it happens that
    # one combined area of # and $ equals it, then we can all fill it with
    longest_char = len(word)
    found = False
    matches = []
    while not found:
        for match in re.finditer(r'[\?\#]{%s}' % longest_char, word):
            found = True
            matches.append(match)
        if not found:
            longest_char -= 1
    if len(matches) == len(occurences):
        if longest_char == max_expect:
            for m in matches:
                word = word[:m.start()] + "#"*(longest_char) + word[m.end():]

    # Optimization 3:
    # Take expectations[0] and compare it to the number of "#" in the first non-"." elements
    # word = reduce(word, expectations)

    # We catch again the occurences of longest chars
    longest_char = len(word)
    found = False
    while longest_char >= max_expect:
        ifound = find_all(word, "#"*longest_char)
        if len(list(ifound))>0:
            break
        longest_char -= 1
    match_occurences = []
    if len(ifound) == len(occurences):
        for i in ifound:
            word = word[:i-1] + "." + word[i:i+longest_char] + "." + word[i+1+longest_char:]
            match_occurences.append([i, i+longest_char])

    print("chars after ", word, expectations)
    return word, occurences, match_occurences

def evaluate(word, expectations):
    """Return true if a word matches expectations

    where word is a "....####.#.#.#.##.#.#."
    and expectations is (1,1,3,2,3)
    """
    if word == "" and not expectations:
        return True
    if word == "" and expectations:
        return False
    if word[0] == ".":
        return evaluate(word[1:], expectations)
    if not expectations:
        return False
    # If we're here it means word[0] is a #
    if expectations[0] == 1:
        # print(word, expectations)
        return (word == "#" or word[1] == ".") and evaluate(word[1:], expectations[1:])

    if word[1] == ".":
        return False
    exp = expectations.copy()
    exp[0] -= 1
    return evaluate(word[1:], exp)


def compute_total(chars, nb_expectations, expectations):
    local_total = 0
    total_unknown = chars.count("?")
    total_filled = chars.count("#")
    unknown_positions = []

    for index, char in enumerate(chars):
        if char == "?":
            unknown_positions.append(index)

    to_fill = nb_expectations - total_filled

    if not unknown_positions and evaluate(chars, expectations.copy()):
        return 1

    for i0, i in enumerate(combinations(range(total_unknown), to_fill)):
        mycopy = chars
        for index, j in enumerate(unknown_positions):
            if index in i:
                mycopy = mycopy[:j] + "#" + mycopy[j+1:]
            else:
                mycopy = mycopy[:j] + "." + mycopy[j+1:]
        if evaluate(mycopy, expectations.copy()):
            local_total += 1
    return local_total


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()

    total = 0
    for row in data.split("\n"):
        start = time.now()

        chars, data = row.split(" ")

        chars = chars+"?"+chars+"?"+chars+"?"+chars+"?"+chars
        print("chars before", chars)
        data = data + "," + data + "," + data + "," + data + "," + data 
        expectations = [int(i) for i in data.split(",")]
        total_expectations = sum(expectations)
        chars, occurences, match_occurences = transform(chars, expectations)

        if len(occurences) != len(match_occurences):
            local_total = compute_total(chars, total_expectations, expectations)
        if len(occurences) == len(match_occurences):
            local_total = 1
            # Occurences will go [0, i1] then [i1+1, i2] then ... then [iN, len()]
            # Match_occurences will go [0, j1] then [j1+1, j2] then ... then [jN, len()]
            for i in range(len(occurences)+1):
                if i == 0:
                    occ = expectations[:occurences[0]]
                    subchar = chars[0:match_occurences[i][0]]
                elif i == len(occurences):
                    occ = expectations[occurences[-1]+1:]
                    subchar = chars[match_occurences[-1][1]+1:]
                else:
                    occ = expectations[occurences[i-1]+1:occurences[i]]
                    subchar = chars[match_occurences[i-1][1]:match_occurences[i][0]]
                local_total *= compute_total(subchar, sum(occ), occ)
        print(local_total, "found in", time.now() - start, "\n")
        total += local_total
    print(total)