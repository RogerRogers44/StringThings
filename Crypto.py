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
