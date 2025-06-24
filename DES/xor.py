def XOR(bits1,bits2):
	"""perform a XOR operation and return the output"""
  # Assuming both bit string of same length
	xor_result = ""
	for index in range(len(bits1)):
		if bits1[index] == bits2[index]: 
			xor_result += '0'
		else:
			xor_result += '1'
	return xor_result
bits1 = '1100'
bits2 = '1010'
# print XOR(bits1,bits2)
# output: '0110'