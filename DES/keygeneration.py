def apply_PC1(pc1_table,keys_64bits):
 """ This function takes Permutation table and initial key as input and return 56 bits key as output"""
 keys_56bits = ""
 for index in pc1_table:
  keys_56bits += keys_64bits[index-1] 
# Python list index start with 0
# so index -1 will cover the difference between the index
 return keys_56bits


PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
keys_64bits = "0001001100110100010101110111100110011011101111001101111111110001"
keys_56bits = apply_PC1(PC1,keys_64bits)
#Output: 11110000110011001010101011110101010101100110011110001111