def circular_left_shift(bits,numberofbits):
 """This method will circularly shift the given bit string according to the number of bits"""
 shiftedbits = bits[numberofbits:] + bits[:numberofbits]
 return shiftedbits
#circularShiftedBits = circular_left_shift(bits,numberofbits)