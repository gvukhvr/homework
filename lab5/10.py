import re

def camel_to_snake(camel_case):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()

with open("row.txt", "r") as file:
    content = file.read()

print("Words in Snake Case:")
print(camel_to_snake(content))
