sentence = "Python is fun and Python is powerful and Python is useful".split()

occurences = {}

for word in sentence:
    occurences[word] = occurences.get(word, 0) + 1

for word, occur in occurences.items():
    print(f"{word}: {occur}")
