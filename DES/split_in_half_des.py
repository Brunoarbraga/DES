from initial_permutation import *

M = '0123456789ABCDEF'

plaintext = hexTobinary(M)
#print plaintext
p_plaintext = apply_initial_p(INITIAL_PERMUTATION_TABLE,plaintext)
#print p_plaintext
## output:

# 0000000100100011010001010110011110001001101010111100110111101111
# 1100110000000000110011001111111111110000101010101111000010101010

def spliHalf(binarybits):
	return binarybits[:32],binarybits[32:]

L0,R0 = spliHalf(p_plaintext)
#print L0,R0

#Output
#'11001100000000001100110011111111' '11110000101010101111000010101010'