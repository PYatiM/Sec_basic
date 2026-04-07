def merge_files(output_file, *input_files):
    import sys
    words = set()
    for file in input_files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            words.update(line.strip() for line in f if line.strip())

    with open(output_file, 'w') as f:
        for word in sorted(words):
            f.write(word + '\n')

