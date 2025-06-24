PERMUTATION_TABLE = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
		                 2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def apply_Permutation(permutation_table,sbox_32bits):
	""" It takes Sboxes output and a permutation table and return 32 bit binary string"""
	final_32bits = ""
	for index in permutation_table:
		final_32bits += sbox_32bits[index-1]
	return final_32bits