from libraries import *

def cipher_color_hashing(ciphertext_list):
	
	return [ColorHash(i).hex for i in ciphertext_list] 	
		
def cipher_digest_table(ciphertext_list):
	hash_table = {}
	
	color_hash_cipher = cipher_color_hashing(ciphertext_list)
	
	for i in range(len(ciphertext_list)):
		hash_table.update({ciphertext_list[i]:color_hash_cipher[i]})
		
	return hash_table	
		
		#if i == 0:
		#	hex_string = '#' + parse.parse_hex(add(color_hash_cipher[i],hex_code_list[i]).hex)
		#	hash_table.update({ciphertext_list[i]:hex_string})
			
		#if i == 1:
		#	hex_string = '#' + parse.parse_hex(invert(color_hash_cipher[i]).hex)
		#	hash_table.update({ciphertext_list[i]:hex_string})
		
		#if i == 2:
		#	hex_string = '#' + parse.parse_hex(subtract(color_hash_cipher[i],hex_code_list[i]).hex)
		#	hash_table.update({ciphertext_list[i]:hex_string})

		#if i == 3:
		#	hex_string = '#' + parse.parse_hex(complement(color_hash_cipher[i]).hex)
		#	hash_table.update({ciphertext_list[i]:hex_string})
	
	








