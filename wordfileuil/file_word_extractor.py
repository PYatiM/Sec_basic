import re
def extractor(file)
    with open(file) as f:
        text = f.read()

    words = re.findall(r'\b\w+\b', text)
    return set(words)