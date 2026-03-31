def clean_wordlist(input_file, output_file):
    with open(input_file, "r") as f:
        words = set(line.strip() for line in f)

    with open(output_file, "w") as f:
        for word in sorted(words):
            f.write(word + "\n")

