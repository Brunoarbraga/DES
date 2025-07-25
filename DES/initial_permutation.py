def hexTobinary(hexdigits):
	binarydigits = ""
	for hexdigit in hexdigits:
		binarydigits += bin(int(hexdigit,16))[2:].zfill(4)
	return binarydigits



INITIAL_PERMUTATION_TABLE = ['58 ', '50 ', '42 ', '34 ', '26 ', '18 ', '10 ', '2',
			 '60 ', '52 ', '44 ', '36 ', '28 ', '20 ', '12 ', '4',
			 '62 ', '54 ', '46 ', '38 ', '30 ', '22 ', '14 ', '6', 
			'64 ', '56 ', '48 ', '40 ', '32 ', '24 ', '16 ', '8', 
			'57 ', '49 ', '41 ', '33 ', '25 ', '17 ', '9 ', '1',
			 '59 ', '51 ', '43 ', '35 ', '27 ', '19 ', '11 ', '3',
			 '61 ', '53 ', '45 ', '37 ', '29 ', '21 ', '13 ', '5',
			 '63 ', '55 ', '47 ', '39 ', '31 ', '23 ', '15 ', '7']

def apply_initial_p(P_TABLE, PLAINTEXT):
	permutated_M = ""
	for index in P_TABLE:
		permutated_M += PLAINTEXT[int(index)-1]
	return permutated_M

M = '0123456789ABCDEF'

plaintext = hexTobinary(M)
#print plaintext
#print apply_initial_p(INITIAL_PERMUTATION_TABLE,plaintext)

## output:

# 0000000100100011010001010110011110001001101010111100110111101111
# 1100110000000000110011001111111111110000101010101111000010101010