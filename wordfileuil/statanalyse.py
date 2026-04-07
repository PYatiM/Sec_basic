def analyze(file):
    from collections import Counter
    lengths = []
    chars = Counter()

    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            lengths.append(len(word))
            chars.update(word)

    print("Total words:", len(lengths))
    print("Min length:", min(lengths))
    print("Max length:", max(lengths))
    print("Average length:", sum(lengths)/len(lengths))
    print("Most common chars:", chars.most_common(10))

