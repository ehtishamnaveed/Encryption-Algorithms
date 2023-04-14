from Functions import *

# Getting 10 bit key from User 
key = getKey()
text = getText()
# key = '1001001110'
# text = '10100001'

print('----------------------------- Generating Keys -----------------------------')
# -------------------------------------- Applying 10 Permutation
p_10 = [3,5,2,7,4,10,1,9,8,6]
key = apply_Permutation(key,p_10)  
print('10 Permutation: ',key)

# Dividing the keys in '2 five-bits'
print('\nDividing the keys in \'2 five-bits\'')
left_side , right_side = divide(key,int(len(key)/2))
print('Left side: ',left_side)
print('Right side: ',right_side)

# Applying left shift by 1
print('\nApplying Left shift by 1')
left_side = left_shift(left_side,1)
right_side = left_shift(right_side,1)
print('Left Side: ',left_side)
print('Right Side: ',right_side)

# -------------------------------------- Applying 8 Permutation to get KEY-1
p_8 = [6,3,7,4,8,5,10,9]
key1 = apply_Permutation(left_side+right_side,p_8)
print('\n8 Permutation for Key-1: ',key1)

# Applying left shift by 2
print('\nApplying Left shift by 2')
left_side = left_shift(left_side,2)
right_side = left_shift(right_side,2)
print('Left Side: ',left_side)
print('Right Side: ',right_side)

# -------------------------------------- Applying 8 Permutation to get KEY-2
p_8 = [6,3,7,4,8,5,10,9]
key2 = apply_Permutation(left_side+right_side,p_8)
print('\n8 Permutation for Key-2: ',key2)

# Printing the keys
print('\n1 Key: ', key1)
print('2 Key: ', key2)


print('\n\n----------------------------- Encrypting -----------------------------')
print('... Using KEY-1')
# -------------------------------------- Applyting Initinal Permutation on Text
IP = [2,6,3,1,4,8,5,7]
text = apply_Permutation(text,IP)
print('Initial Permutation: ',text)

# Dividing the text in '2 five-bits'
print('\nDividing the text in \'2 five-bits\'')
left_side , right_side = divide(text,int(len(text)/2))
# Saving in the value to be used in swapping
left_bits = left_side
right_bits = right_side
print('Left side: ',left_side)
print('Right side: ',right_side)

# -------------------------------------- Applyting Expansion Permutation on Text
EP = [4,1,2,3,2,3,4,1]
right_side = apply_Permutation(right_side,EP)
print('\nExpansion Permutation: ',right_side)

# Applying XOR operation with KEY-1
right_side = applyXOR(right_side,key1)
print('\nXOR Operation with KEY-1: ',right_side)

# Dividing the text in '2 four-bits'
print('\nDividing the text in \'2 four-bits\'')
S0 , S1 = divide(right_side,int(len(right_side)/2))
print('S0_BOX: ',S0)
print('S1_BOX: ',S1)

# Applying SBOX
Box0 = [[1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]]

Box1 = [[0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]]

bits = apply_SBOX(S0,Box0)        
bits += apply_SBOX(S1,Box1)
print('\nAfter applying SBOX: ',bits)

# -------------------------------------- Applyting 4 Permutation on Text
p_4 = [2,4,3,1]
bits = apply_Permutation(bits,p_4)
print('\n4 Permutation: ',bits)

# Applying XOR operation with Left side
bits = applyXOR(bits,left_bits)
print('\nXOR Operation with Left Side: ',bits)

# Swapping the right and left side
print('\nNow swapping the Sides, we get')
right_side = bits
left_side = right_bits
right_bits = right_side
print('Left Side: ',left_side)
print('Right Side: ',right_side)

# -----------------------------------------------------------------------
print('\n... Using KEY-2')
# -------------------------------------- Applyting Expansion Permutation on Text
EP = [4,1,2,3,2,3,4,1]
right_side = apply_Permutation(right_side,EP)
print('Expansion Permutation: ',right_side)

# Applying XOR operation with KEY-2
right_side = applyXOR(right_side,key2)
print('\nXOR Operation with KEY-2: ',right_side)

# Dividing the text in '2 four-bits'
print('\nDividing the text in \'2 four-bits\'')
S0 , S1 = divide(right_side,int(len(right_side)/2))
print('S0_BOX: ',S0)
print('S1_BOX: ',S1)

# Applying SBOX
Box0 = [[1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]]

Box1 = [[0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]]

bits = apply_SBOX(S0,Box0)        
bits += apply_SBOX(S1,Box1)
print('\nAfter applying SBOX: ',bits)

# -------------------------------------- Applyting 4 Permutation on Text
p_4 = [2,4,3,1]
bits = apply_Permutation(bits,p_4)
print('\n4 Permutation: ',bits)

# Applying XOR operation with Left side
bits = applyXOR(bits,left_side)
print('\nXOR Operation with Left Side: ',bits)

# combining the left side and right side together
bits += right_bits

# Applying the Inverse Initial Permutation to get the final Cipher Text
IP_1 = [4,1,3,5,7,2,8,6]
cipher = apply_Permutation(bits,IP_1)
print('\nCipher Text: ',cipher)


print('\n\n----------------------------- Decrypting -----------------------------')
print('... Using KEY-2')
# -------------------------------------- Applyting Initinal Permutation on Text
IP = [2,6,3,1,4,8,5,7]
text = apply_Permutation(cipher,IP)
print('Initial Permutation: ',text)

# Dividing the text in '2 five-bits'
print('\nDividing the text in \'2 five-bits\'')
left_side , right_side = divide(text,int(len(text)/2))
# Saving in the value to be used in swapping
left_bits = left_side
right_bits = right_side
print('Left side: ',left_side)
print('Right side: ',right_side)

# -------------------------------------- Applyting Expansion Permutation on Text
EP = [4,1,2,3,2,3,4,1]
right_side = apply_Permutation(right_side,EP)
print('\nExpansion Permutation: ',right_side)

# Applying XOR operation with KEY-1
right_side = applyXOR(right_side,key2)
print('\nXOR Operation with KEY-1: ',right_side)

# Dividing the text in '2 four-bits'
print('\nDividing the text in \'2 four-bits\'')
S0 , S1 = divide(right_side,int(len(right_side)/2))
print('S0_BOX: ',S0)
print('S1_BOX: ',S1)

bits = apply_SBOX(S0,Box0)        
bits += apply_SBOX(S1,Box1)
print('\nAfter applying SBOX: ',bits)

# -------------------------------------- Applyting 4 Permutation on Text
p_4 = [2,4,3,1]
bits = apply_Permutation(bits,p_4)
print('\n4 Permutation: ',bits)

# Applying XOR operation with Left side
bits = applyXOR(bits,left_bits)
print('\nXOR Operation with Left Side: ',bits)

# Swapping the right and left side
print('\nNow swapping the Sides, we get')
right_side = bits
left_side = right_bits
right_bits = right_side
print('Left Side: ',left_side)
print('Right Side: ',right_side)

# -----------------------------------------------------------------------
print('\n... Using KEY-1')
# -------------------------------------- Applyting Expansion Permutation on Text
EP = [4,1,2,3,2,3,4,1]
right_side = apply_Permutation(right_side,EP)
print('Expansion Permutation: ',right_side)

# Applying XOR operation with KEY-2
right_side = applyXOR(right_side,key1)
print('\nXOR Operation with KEY-2: ',right_side)

# Dividing the text in '2 four-bits'
print('\nDividing the text in \'2 four-bits\'')
S0 , S1 = divide(right_side,int(len(right_side)/2))
print('S0_BOX: ',S0)
print('S1_BOX: ',S1)

# Applying SBOX
Box0 = [[1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]]

Box1 = [[0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]]

bits = apply_SBOX(S0,Box0)        
bits += apply_SBOX(S1,Box1)
print('\nAfter applying SBOX: ',bits)

# -------------------------------------- Applyting 4 Permutation on Text
p_4 = [2,4,3,1]
bits = apply_Permutation(bits,p_4)
print('\n4 Permutation: ',bits)

# Applying XOR operation with Left side
bits = applyXOR(bits,left_side)
print('\nXOR Operation with Left Side: ',bits)

# combining the left side and right side together
bits += right_bits

# Applying the Inverse Initial Permutation to get the final Cipher Text
IP_1 = [4,1,3,5,7,2,8,6]
text = apply_Permutation(bits,IP_1)
print('\nPlain Text: ',text)

input('')