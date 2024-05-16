import string

with open("message.txt") as filp:
    contents = filp.read()

uppercase_key = "DECKFMYIQJRWTZPXGNABUSOLVH"
lowercase_key = uppercase_key.lower()

flag = []

for character in contents:
    if character.isupper():
        position = uppercase_key.index(character)
        flag.append(string.ascii_uppercase[position])
    elif character.islower():
        position = lowercase_key.index(character)
        flag.append(string.ascii_lowercase[position])
    else:
        flag.append(character)



flag = "".join(flag)
print(flag.split()[-1])
#print(string.ascii_uppercase + string.ascii_lowercase)

