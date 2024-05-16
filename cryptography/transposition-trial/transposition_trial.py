

with open("message.txt") as filp:
    contents = filp.read()

# Change in every block of 3 letters

for i in range(0, len(contents), 3):
    group = contents[i : i + 3]
    letter1, letter2, letter3 = group
    # Since by checking the group, we found that the order by should be : 3==>1==>2
    print(letter3 + letter1 + letter2, end="")

#print(contents)


'''
Option 2 upgrade
flag = []

# Change in every block of 3 letters

for i in range(0, len(contents), 3):
    group = contents[i : i + 3]
    letter1, letter2, letter3 = group
    flag.append(letter3 + letter1 + letter2)

flag = "".join(flag).split()[-1]
print(flag)
#print(contents

'''