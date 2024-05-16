# Python3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

# initializing string

str2hash = input("Enter the quotes you want to hash: ")

# encoding using uncode()
# then sending to md5()

result = hashlib.md5(str2hash.encode())


# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())
