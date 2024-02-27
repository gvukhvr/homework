#7
def change(snakestring):
    words = snakestring.split('_')
    camelstring = ''.join(word.capitalize() for word in words)
    return camelstring

with open("row.txt", "r") as file:
    content = file.read()

words = content.split()
camel_words = [change(word) for word in words]

print("Words in Camel Case:")
for word in camel_words:
    print(word)
