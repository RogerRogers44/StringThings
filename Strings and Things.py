# Strings

# Concatenation
# 2 or more strings and put them together
# literally just a plus

firstName = "Wilma"
lastName = "Flint"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition

print("Hip"*10 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("Merrily "*4)
    print("Life is but a dream")


rowYourBoat()

# Indexing

name = "Roy G Biv"
firstCharacter = name[0]
print(firstCharacter)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])
print(name[-1])
print(name[-3])

for i in range(4, len(name)):
    print("HI", name[i])

# Slicing
# Second number is up to, but not including, where you stop
print(name[4:-3])

for i in range(0, len(name)):
    print("BOO", name[0:i])

# Searching

print("Biv" in name)

if "y" not in name:
    print("y in not in name")
else:
    print("y is in name")


# Character Based functions

print(chr(75))

from mapper import *
print(letterToIndex('m'))

print(indexToLetter(24))


# crypto
from Crypto import *


print(scramble2Encrypt("THE MEETING IS AT FIVE OCLOCK"))
print(scramble2Encrypt("H ETN SA IEOLCTEMEIGI TFV COK"))
print(scrambleToDecrypt(" T AIOCEEG F OHENS ELTMIITVCK"))
print(scrambleToDecrypt("H ETN SA IEOLCTEMEIGI TFV COK"))
print(scrambleToDecrypt("H ETN SA IEOLCTEMEIGI TFV COK"))