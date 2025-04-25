from libraries import *


def unhashing_cipher_dict(digest_values, hex_code_list):

	strands_color_hash_values = []

	for k in range(len(digest_values)):
		if k == 0:
			hex_string = '#' + parse.parse_hex(subtract(digest_values[k],hex_code_list[k]).hex)
			strands_color_hash_values.append(hex_string)
		
			#print(hex_string)
			#print(color_cipher)
			
		if k == 1:
			hex_string = '#' + parse.parse_hex(invert(digest_values[k]).hex)
			strands_color_hash_values.append(hex_string)

		if k == 2:
			hex_string = '#' + parse.parse_hex(add(digest_values[k],hex_code_list[k]).hex)
			strands_color_hash_values.append(hex_string)
		
			#print(hex_string)
			#print(color_cipher)

		if k == 3:
			hex_string = '#' + parse.parse_hex(complement(digest_values[k]).hex)
			strands_color_hash_values.append(hex_string)
	
	return strands_color_hash_values
	

def verify(strands_color_hash_values, color_hash_cipher):

	for k in range(len(strands_color_hash_values)):
		
		if k == 0:
			color_cipher = color_hash_cipher[k]
			hex_string = strands_color_hash_values[k]
			if (hex_string[1:3] == color_cipher[1:3]) or (hex_string[3:5] == color_cipher[3:5]) or (hex_string[5:7] == color_cipher[5:7]):
				print('Vertified strand 1')
				
		if k == 1:
			color_cipher = color_hash_cipher[k]
			hex_string = strands_color_hash_values[k]
			if hex_string == color_hash_cipher[k]:
				print('Vertified strand 2')		
				
		if k == 2:
			color_cipher = color_hash_cipher[k]
			hex_string = strands_color_hash_values[k]
			if (hex_string[1:3] == color_cipher[1:3]) or (hex_string[3:5] == color_cipher[3:5]) or (hex_string[5:7] == color_cipher[5:7]):
				print('Vertified strand 3')	
				
		if k == 3:
			color_cipher = color_hash_cipher[k]
			hex_string = strands_color_hash_values[k]
			if hex_string == color_hash_cipher[k]:
				print('Vertified strand 4')
				
	
	
	
	
