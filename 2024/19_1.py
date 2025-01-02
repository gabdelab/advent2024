FILENAME = "data/19.txt"

from collections import defaultdict
def look_for(sentence, words_dict):
    found = False
    to_look_for = []
    if sentence == "":
        return True
    if len(sentence) == 1:
        return sentence != "b"
    to_check = words_dict[sentence[0]][sentence[1]]
    to_check.extend(["u", "w", "g", "r"])
    for word in to_check:
        if len(word) > len(sentence):
            continue
        if word == sentence:
            return True
        if word == sentence[:len(word)]:
            look_for_word = look_for(sentence[len(word):], words_dict)
            to_look_for.append(look_for_word)
            if look_for_word:
                return True
    return any([i for i in to_look_for])


data = []
with open(FILENAME, "r") as file:
    wd = file.read().split("\n\n")
    words = [i.strip() for i in wd[0].split(",")]
    sentences = [i.strip() for i in wd[1].split("\n")]

words_dict = defaultdict(lambda: defaultdict(list))
for i in words:
    if len(i) > 1:
        words_dict[i[0]][i[1]].append(i)


total_found = 0
for sentence in sentences:
    print("looking for", sentence)
    found = look_for(sentence, words_dict)
    if found:
        print(sentence, "found")
        total_found += 1
    else:
        print(sentence, "KO NOT FOUND")
print(total_found)
