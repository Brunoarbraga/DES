from final_subkey_generation import *
from calculate_function_f import *
from apply_inverse_permutation import *

def XOR(bits1,bits2):	
	xor_result = ""
	for index in range(len(bits1)):
		if bits1[index] == bits2[index]:
			xor_result += '0'
		else:
			xor_result += '1'
	return xor_result
# Generate round keys Part- 1 of blog post

roundkeys = generate_keys(key_64bits)
# Suppose initial R and L value is 
R = '11001100000000001100110011111111'  
L = '11110000101010101111000010101010'

for round in range(16):
	# functionF() is implemented in part 2
	newR = XOR(L,functionF(R, roundkeys[round]) )
	newL = R
	# Swapping the value for next round
	R = newR
	L = newL

cipher = apply_initial_p(INVERSE_PERMUTATION_TABLE, R+L)

#print cipher