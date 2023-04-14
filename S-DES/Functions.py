# Input for 10-bit KEY from user Function
def getKey():
	while(1):
		key = input("Enter a 10-digit key: ")
		if len(key) == 10:
			break
		else:
			print("Error: Please Ener 10 digit key.")
			continue
	return key

# Imput for the 8-bit plain text from user Function
def getText():
	while(1):
		text = input("Enter a 8-digit text: ")
		if len(text) == 8:
			break
		else:
			print("Error: Please Ener 8 digit text.")
			continue
	return text

# A Permutation Function
def apply_Permutation(key,permutation):
	permutedKey = []
	for index in range(len(permutation)):
		value = permutation[index]
		permute = key[value-1]
		permutedKey.append(permute)
	return permutedKey

# Left Shift Function
def left_shift(key, shift_amount):
	newKey = []
	for index in range(len(key)):
		if (index - shift_amount < 0):
			newKey.insert(4 , key[index])
		else:
			newKey.insert(index - shift_amount , key[index])
	return newKey

# Divide into 2 parts Function 
def divide(key,length):
	leftSide= key [:length]
	rightSide= key [length:]
	return leftSide , rightSide

# XOPR operation Function
def applyXOR(text,key):
	finalValue = []
	for index in range(len(text)):
		if text[index] == key[index]:
			finalValue.append('0')
		else:
			finalValue.append('1')
	return finalValue

# Applying SBOX Function
def apply_SBOX(key,box):
    rowValue , columnValue = divide(key,int(len(key)/2)) # Dividing the fours bits in '2 two-bits'
    rowValue = int(''.join(rowValue), 2)
    columnValue = int(''.join(columnValue), 2)
    value = box[rowValue][columnValue]
    value = bin(value)[2:].zfill(2)
    return list(value)