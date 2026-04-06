# mutate_words.py
def mutate(word):
    variations = set()
    variations.add(word)
    variations.add(word.capitalize())
    variations.add(word.upper())
    variations.add(word + "123")
    variations.add("@" + word)
    variations.add(word + "!")
    variations.add(word[::-1])
    return variations

def generate(input_file, output_file):
    result = set()
    with open(input_file, 'r') as f:
        for line in f:
            word = line.strip()
            result.update(mutate(word))

    with open(output_file, 'w') as f:
        for word in result:
            f.write(word + '\n')

if __name__ == "__main__":
    generate("input.txt", "mutated.txt")