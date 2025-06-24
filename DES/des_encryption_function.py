from apply_inverse_permutation import *
from initial_permutation import *
from final_subkey_generation import *
from calculate_function_f import *
from split_in_half_des import *  
from PIL import Image

M = '0123456789ABCDEF'
key ='12345678ABCEDFF9'

def DES_encrypt(message,key):
	cipher = ""
	# Convert hex digits to binary
	plaintext_bits = hexTobinary(message)
	key_bits = hexTobinary(key)
	# Generate rounds key
	roundkeys = generate_keys(key_bits)
	#### DES steps
	
	## initial permutation
	p_plaintext = apply_initial_p(INITIAL_PERMUTATION_TABLE,plaintext_bits)
	## split in tow half
	L,R = spliHalf(p_plaintext)
	## start rounds
	for round in range(16):
		newR = XOR(L,functionF(R, roundkeys[round]))
		newL = R
		R = newR
		L = newL
	cipher = apply_initial_p(INVERSE_PERMUTATION_TABLE, R+L)
	return cipher

# Convert binary string to bytes
def bin_to_bytes(bin_str):
	return int(bin_str, 2).to_bytes(len(bin_str) // 8, byteorder='big')

# Encrypt image file
def encrypt_image(path, output_path, key):
	im = Image.open(path).convert('RGB')
	img_bytes = im.tobytes()
	img_hex = img_bytes.hex()

	# Split hex into 16-char blocks (64 bits = 8 bytes)
	blocks = [img_hex[i:i+16] for i in range(0, len(img_hex), 16)]

	encrypted_blocks = []
	for block in blocks:
		if len(block) < 16:
			block = block.ljust(16, '0')  # pad last block with 0s
		bin_result = DES_encrypt(block, key)
		encrypted_blocks.append(bin_result)

	# Convert binary strings to bytes
	encrypted_bytes = b''.join([bin_to_bytes(b) for b in encrypted_blocks])

	# Recreate image
	encrypted_np = bytearray(encrypted_bytes[:len(img_bytes)])
	encrypted_img = Image.frombytes('RGB', im.size, bytes(encrypted_np))
	encrypted_img.save(output_path)
	encrypted_img.show()

#encrypt_image('../lenna.png', 'lenna_encrypted.png', key)