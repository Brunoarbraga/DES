import textwrap
from sbox import *

def split_in_6bits(XOR_48bits):
	"""split 48 bits into 6 bits each """
	list_of_6bits = textwrap.wrap(XOR_48bits,6)
	return list_of_6bits

## Below are some supportive function used for smooth the process

def get_first_and_last_bit(bits6):
	"""Return first and last bit from a binary string"""
	twobits = bits6[0] + bits6[-1] 
	return twobits

def get_middle_four_bit(bits6):
	"""Return first and last bit from a binary string"""
	fourbits = bits6[1:5] 
	return fourbits

def binary_to_decimal(binarybits):
	""" Convert binary bits to decimal"""
	# helps during list access
	decimal = int(binarybits,2)
	return decimal

def decimal_to_binary(decimal):
	""" Convert decimal to binary bits"""
	binary4bits = bin(decimal)[2:].zfill(4)
	return binary4bits

def sbox_lookup(sboxcount,first_last,middle4):
	""" take three parameter and access the Sbox accordingly and return the value"""
	d_first_last = binary_to_decimal(first_last)
	d_middle = binary_to_decimal(middle4)
	
	sbox_value = SBOX[sboxcount][d_first_last][d_middle]
	return decimal_to_binary(sbox_value)

#Example:
bits6 = '100000'
first_last = get_first_and_last_bit(bits6)  # '10' -> 2
middle4 = get_middle_four_bit(bits6)  # '0000' -> 0

# suppose we are processing the first 6-bit so the sbox number will be sboxcount = 1
sboxcount = 1
result = sbox_lookup(sboxcount,first_last,middle4) # i.e. 3rd row and first column --> 4 i.e. '0100'