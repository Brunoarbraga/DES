#def apply_compression(pc2_table,keys_56bits):
def apply_PC2(pc2_table,keys_56bits):
 """ This will take Compression table and combined both half as input and return a 48-bits string as output"""
 keys_48bits = ""
 for index in pc2_table:
  keys_48bits += keys_56bits[index-1]
 return keys_48bits
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
#to call this function there must be left_half and right_half
#subkey = apply_compression(PC2,left_half + right_half)
#subkey = apply_PC2(PC2,left_half + right_half)