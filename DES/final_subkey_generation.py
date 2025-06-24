from keygeneration import *
from split_in_half import *
from circular_left_shift import *
from apply_compression import *

def generate_keys(key_64bits):
 round_keys = list() 
 pc1_out = apply_PC1(PC1,key_64bits) 
 L0,R0 = split_in_half(pc1_out)
 for roundnumber in range(16):
  newL = circular_left_shift(L0,round_shifts[roundnumber])
  newR = circular_left_shift(R0,round_shifts[roundnumber])
  roundkey = apply_PC2(PC2,newL+newR)
  round_keys.append(roundkey)
  L0 = newL
  R0 = newR
 return round_keys
round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
key_64bits = "0001001100110100010101110111100110011011101111001101111111110001"
subkeys = generate_keys(key_64bits)
# The subkeys will have all 16 keys as Python list
#print subkeys