from apply_expansion import *
from xor import *
from sbox_lookup import *
from apply_final_permutation import *

def functionF(pre32bits, key48bits):	
	"""This is main function to perform function F """
	result = ""
	expanded_left_half = apply_Expansion(EXPANSION_TABLE,pre32bits)
	xor_value = XOR(expanded_left_half,key48bits)
	bits6list = split_in_6bits(xor_value)
	for sboxcount, bits6 in enumerate(bits6list):
		first_last = get_first_and_last_bit(bits6)
		middle4 = get_middle_four_bit(bits6)
		sboxvalue = sbox_lookup(sboxcount,first_last,middle4)
		result += sboxvalue
	final32bits = apply_Permutation(PERMUTATION_TABLE,result)	
	return final32bits