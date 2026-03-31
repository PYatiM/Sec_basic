import re

with open("file.txt") as f:
    text = f.read()

words = re.findall(r'\b\w+\b', text)
print(set(words))