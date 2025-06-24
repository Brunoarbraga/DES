EXPANSION_TABLE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,
16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

def apply_Expansion(expansion_table,bits32):
	""" This will take expansion table and 32-bit binary string as input and output a 48-bit binary stirng"""
	bits48 = ""
	for index in expansion_table:
		bits48 += bits32[index-1]
	return bits48
bits32 = '11110000101010101111000010101010'
out_bits48 = apply_Expansion(EXPANSION_TABLE,bits32)
# print out_bits48
# 011110100001010101010101011110100001010101010101