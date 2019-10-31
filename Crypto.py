# Transposition Cipher

# encryption function


def scramble2Encrypt(plainText):
    evenChar = ""
    oddChar = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChar = evenChar + ch
        else:
            oddChar = oddChar + ch
        charCount = charCount + 1
    cipherText = oddChar + evenChar
    return cipherText



def scrambleToDecrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:] # halflength to the end
    oddChars = cipherText[:halfLength] # 0 to halflength - 1
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


from mapper import *

def CaesarCypherEncrypt(plaintext):
    for i in range(len(plaintext)):
        firstCharacter = plaintext[0]
        a = letterToIndex(firstCharacter) - 3
        firstencryptcharacter = indexToLetter(a)
        return firstencryptcharacter
