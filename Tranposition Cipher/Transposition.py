def encrypt(plainText, rowNo):
	# Creating an empty 2D matric 
	matrix = generateMatrix(rowNo, plainText)
	# Converts text elements as individual characters in matrix
	matrix = fillMatrixforEncryption(matrix,plainText)
	showMatrix(matrix)
	# Combinating elements in a single string
	cipher = catenateforEncrypting(matrix)
	return cipher

def decrypt(cipherText, rowNo):
	# Creating an empty 2D matric 
	matrix = generateMatrix(rowNo, cipherText)
	# Converts text elements as individual characters in matrix
	matrix = fillMatrixforDecryption(matrix,cipherText)
	showMatrix(matrix)
	# Combinating elements in a single string
	plainText = catenateforDecrypting(matrix)
	return plainText

# This function helps to create an empty list with required ammount of Rows and Columns
def generateMatrix(rows, text):
    columns = round(len(text) / rows)
    emptyList = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(' ')
        emptyList.append(row)
    return emptyList

# This function converts the input into a matrix, character by character, for Encryption
def fillMatrixforEncryption(matrix,text):
	rows = len(matrix)
	columns = len(matrix[0])
	index = 0 

	# assigning the Characters in matrix in Row order
	for y_axis in range(columns):
		for x_axis in range(rows):
			try:
				matrix[x_axis][y_axis] = text[index]
				index += 1
			except IndexError:
				break
	return matrix

# This function converts the input into a matrix, character by character, for Decryption
def fillMatrixforDecryption(matrix, text):
    rows = len(matrix)
    columns = len(matrix[0])
    index = 0

    # assigning the Characters in matrix in Column order
    for x_axis in range(rows):
        for y_axis in range(columns):
            try:
                matrix[x_axis][y_axis] = text[index]
                index += 1
            except IndexError:
                break
    return matrix

# It combines all th matrix values in a single string, row wise, for Encryption
def catenateforEncrypting(matrix):
    cipher = ''
    for row in matrix:
        for element in row:
            cipher += element
    return cipher

# It combines all th matrix values in a single string, column wise, for Decryption
def catenateforDecrypting(matrix):
    cipher = ''
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            cipher += matrix[row][col]
    return cipher

# Print Elements of Matrin
def showMatrix(matrix):
	for index in range(len(matrix)):
		print(matrix[index])