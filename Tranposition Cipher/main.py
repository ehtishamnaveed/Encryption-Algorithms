from Transposition import *

plainText = input("Enter your Text: ")
rowNo = int(input("How many Rows (KEY): "))

print("-----------------------------------------------------------")
print('\n*Encrypting')
print("\nFirstly we will create an empty 2Dimensional array.")
print("The Key will be the row size the User will enter.")
print("After that we will calculate the columns size by Length(PlainText)/Row size")
print("Then will we start to write the plain text in Matrix character by character(Spaces included) in Column order(↓)")
print("After writing Characters in column order, We starts to catenate the characters by reading in Row Order\n")
print("The PLain Text is:",plainText)
# Encryption
cipher = encrypt(plainText, rowNo)
print('\nCipher Text:',cipher)

print("\n-----------------------------------------------------------")

print('\n*Decrypting')
print("\nFor Decryption we will again calculate the matrix size by using Length(CipherText)/Row Size")
print("Then we will start to fill the Matrix character by character(Spaces included) in Row order(→)")
print("After writing Characters in Row order, We starts to catenate the characters by reading in Column Order\n")
print("The cipher Test is:",cipher)
# Decryption
plainText = decrypt(cipher, rowNo)
print('\nPlain Text:',plainText)