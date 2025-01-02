FILENAME = "data/19.txt"

cached = {}

def look_for(sentence):
    global cached, words
    # Return the number of different paths that allow to find the sentence
    if sentence in cached.keys():
        return cached[sentence]
    if sentence == "":
        cached[sentence] = 1
        return 1
    if len(sentence) == 1:
        found = int(sentence in words)
        cached[sentence] = found
        return found
    results = []
    for word in words:
        if len(sentence) < len(word):
            continue
        if word == sentence[:len(word)]:
            results.append(look_for(sentence[len(word):]))
    cached[sentence] = sum(results)
    return sum(results)

data = []
with open(FILENAME, "r") as file:
    wd = file.read().split("\n\n")
    words = [i.strip() for i in wd[0].split(",")]
    sentences = [i.strip() for i in wd[1].split("\n")]

total_found = 0
for sentence in sentences:
    found = look_for(sentence)
    if found > 0:
        print(sentence, "found", found, "times")
        total_found += found
    else:
        print(sentence, "KO NOT FOUND")
print(total_found)
