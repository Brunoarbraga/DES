HEX_to_Binary = {'0':'0000',
		 '1':'0001',
		 '2':'0010',
		 '3':'0011',
		 '4':'0100',
		 '5':'0101',
		 '6':'0110',
		 '7':'0111',
		 '8':'1000',
		 '9':'1001',
		 'A':'1010',
		 'B':'1011',
		 'C':'1100',
		 'D':'1101',
		 'E':'1110',
		 'F':'1111',
		}


def hexDigit_to_binary_bits(hex_digit):
	binary_4bits = HEX_to_Binary[hex_digit]
	return binary_4bits

def hexString_to_binary_bits1(hex_string):
	binary_bits = ""
	for hex_digit in hex_string:
		binary_bits += hexDigit_to_binary_bits(hex_digit)
	return binary_bits

def hexString_to_binary_bits2(hexdigits):
	binarydigits = ""
	for hexdigit in hexdigits:
		binarydigits += bin(int(hexdigit,16))[2:].zfill(4)
	return binarydigits
		
M = '0123456789ABCDEF' # plaintext in hexdecimal 16 digits so 64 bits 
#print hexString_to_binary_bits1(M)
# Output: 0000000100100011010001010110011110001001101010111100110111101111
#print hexString_to_binary_bits2(M)
# Output: 0000000100100011010001010110011110001001101010111100110111101111