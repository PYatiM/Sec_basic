=def extractor(file)
    import re
    with open(file) as f:
        text = f.read()

    words = re.findall(r'\b\w+\b', text)
    return set(words)