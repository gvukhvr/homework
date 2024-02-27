#8
import re

with open("row.txt", "r") as file:
    content = file.read()

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

print("Substrings after splitting at uppercase letters:")
for line in content.split('\n'):
    substrings = split_at_uppercase(line.strip())
    for substring in substrings:
        print(substring)
