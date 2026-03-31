def generate(base):
    variations = []
    for i in range(100):
        variations.append(base + str(i))
    return "\n".join(variations)
