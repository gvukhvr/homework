import re

with open("row.txt", "r") as file:
    content = file.read()

def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

print("String with spaces inserted:")
print(insert_spaces(content))
