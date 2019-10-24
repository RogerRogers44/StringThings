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

