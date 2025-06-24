def split_in_half(keys_56bits):
 """ Split the 56 bits key into two equal half """
 left_keys, right_keys = keys_56bits[:28],keys_56bits[28:]
 return left_keys, right_keys
#left56 , right56 = split_in_half(keys_56bits)