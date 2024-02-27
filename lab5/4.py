#4
import re
with open("row.txt", "r") as file:
    content = file.read()


pattern = re.compile(r'\b[A-Z][a-z]+\b')

matches = pattern.findall(content)
for match in matches:
    print(match)
