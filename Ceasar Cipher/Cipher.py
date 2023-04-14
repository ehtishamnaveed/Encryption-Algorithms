# --------------------------------------------------------------------

def createCipher(text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for char in text.upper():
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + shift) % 26]
    return result

# --------------------------------------------------------------------

def crackCipher(text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    results = []

    for shift_value in range(len(alphabet)):
        result = ''

        for char in text.upper():
            if char in alphabet:
                result += alphabet[(alphabet.index(char) - shift_value -1) % 26]
        # if i > 0:
        results.append(result)
    return results

# --------------------------------------------------------------------

plaintext = input("Enter you Text: ")
encryptingShift = int(input("Enter you Cipher Shift: "))
code = createCipher(plaintext,encryptingShift)

print("\nEncrytpted Text: ",code,"\n\n")
combinations = crackCipher(code)

print("Possible combinations:")
for index, char in enumerate(combinations):
    print("Using Shift:",index+1," --> ", char)

input("Press Any Key to Exit.....")
