#6
import re
with open("row.txt", "r") as file:
    content = file.read()

pattern = re.compile(r'[ ,.]')

matches = re.sub(pattern, ':', content)
for match in matches.split():
    print(match)

