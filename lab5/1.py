#1
import re
with open("row.txt", "r") as file:
    content = file.read()
pattern = re.compile(r'\b[a-z]*a[b]*\b')
matches = pattern.findall(content)
for match in matches:
    print(match)

