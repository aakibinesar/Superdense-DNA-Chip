from libraries import *

#Pre-information
encoding_seq = "".join(list(DNA_coding.DNA_encoding_rules[ECDH.rule].values()))
myAlphabet = DNA_Vigenere.createAlphabet(encoding_seq)
myLines = DNA_Vigenere.createLines(encoding_seq, myAlphabet)
transpose_str = Seq(encoding_seq)
transpose_key = str(transpose_str.complement())
encoding_list = list(encoding_seq)

print("Vigenere key:", encoding_seq)

print("DNA-Vigenere Table:")
for line in myLines:
    lineString = ''.join(line)
    print(lineString)

print("Transpose key:", transpose_key)

###                 ***Main Function***                    ###

def read_in_chunks(file_object, chunk_size=1024):
#    """Lazy function (generator) to read a file piece by piece.
#    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size).strip()
        if not data:
            break
        yield data


with open('bible.txt') as f:
    DNA_str = ''
    for piece in read_in_chunks(f):
        DNA_str += "".join(DNA_coding.DNA_encoded_message(piece))



#input_file = open(sys.argv[1],"r")
#content = input_file.read().strip() #data preprocessing
#input_file.close()


#Alice's part

#Encryption
tic = time.perf_counter()

#DNA_str = "".join(DNA_coding.DNA_encoded_message(content))

Encryption_key = Secret_Keys.encryption_key(ECDH.A_shared_key)

# Encryption
if len(Encryption_key) > len(DNA_str):
	Encryption_key = Encryption_key[0:len(DNA_str)]
	#print("Encryption key:", Encryption_key)
	encrypted_message, switches = DNA_Vigenere.encrypt(DNA_str, Encryption_key, encoding_seq)
else:
	#print("Encryption key:", Encryption_key)
	encrypted_message, switches = DNA_Vigenere.encrypt(DNA_str, Encryption_key, encoding_seq)


#print(encrypted_message)
#print(switches)

# Columnar Transpose
#Final_ciphertext, col_transpose_dict_encrypt = Columnar_Transposition.col_transpose_encryption(encrypted_message, transpose_key)

#print("Final Ciphertext: " + Final_ciphertext)

#Rail Fence Transpose
Final_ciphertext, rail_fence_transpose_dict = Rail_Fence.encryptRailFence(encrypted_message, transpose_key)

#print("Final Ciphertext: " + Final_ciphertext)

#sorted dictionary according to key letters
#sorted_rail_fence_transpose_dict = {i: rail_fence_transpose_dict[i] for i in encoding_list}

#print(rail_fence_transpose_dict)

# Hiding the ciphertext strands at different points where the label and value of the block are equal

N = 4 # 4x4 dimension
for row in range(N):
	for column in range(N):
		for i in rail_fence_transpose_dict.keys():
			if i == switches[row][column]:
				switches[row][column] = rail_fence_transpose_dict[i]


			
#print(switches)
						 
toc = time.perf_counter()
elapsed_time = toc - tic
print("Encryption time:", elapsed_time)

#f=open("Encryption_file.txt", "w")
#print('Encryption Time: ', elapsed_time, file=f)
#print("Encrypted message size in megabytes:", (len(encrypted_message) * 2 * 1.25e-7))
#f.close()

#Initial Superdense DNA chip without hashing
Chip.DNA_chip(switches, "Superdense DNA Chip")

#Hashing
tic = time.perf_counter()

ciphertext_list = list(rail_fence_transpose_dict.values())

#print(ciphertext_list)

#color_hash_cipher = Merkle_Tree.hash_data(ciphertext_list)

#print('Color hash values of ciphertext strands: ', color_hash_cipher)

color_hashed_key_dict, hashed_switches = hash_table.hashed_dict(switches, encoding_seq)

#print('Color hash values of key letters: ', color_hashed_key_dict)

#print(hashed_switches)

#key_hex_code_list = list(color_hashed_key_dict.values())

#Final Hash Table
cipher_digest_dict = hashing.cipher_digest_table(ciphertext_list)

Alice_Merkle_Root = Merkle_Tree.merkle_tree(ciphertext_list)

toc = time.perf_counter()
elapsed_time = toc - tic
print("Hashing time:", elapsed_time)

# message : digest/hash/fingerprint
#print('Digest values of ciphertext strands / Final Hash Table: ', cipher_digest_dict) 

digest_values = list(cipher_digest_dict.values())

#Initial Hashed Superdense DNA Chip
Chip.DNA_chip(hashed_switches, "Initial Hashed Superdense DNA Chip")

#Color Hashed Cipher Blocks
Chip.Hashed_chip(digest_values, hashed_switches, "Color Hashed Chip Blocks")

#Final Hashed Superdense DNA Chip
#Chip.Hashed_chip(digest_values, hashed_switches, "Final Hashed Superdense DNA Chip")

#--------------------------------------------------------------------------------------------------------#

#cipher_digest_dict, hashed_switches, [color_hashed_key_dict/key_hex_code_list (pre-information)] 

#Bob's part
encoding_seq = "".join(list(DNA_coding.DNA_encoding_rules[ECDH.rule].values()))
transpose_str = Seq(encoding_seq)
transpose_key = str(transpose_str.complement())
encoding_list = list(encoding_seq)
Decryption_key = Secret_Keys.decryption_key(ECDH.B_shared_key)


#unhashing
digest_values = list(cipher_digest_dict.values())

#strands_color_hash_list = hash_verify.unhashing_cipher_dict(digest_values, key_hex_code_list)

#print('Color hash values of ciphertext strands: ', strands_color_hash_list)

Chip.Hashed_chip(digest_values, hashed_switches, "Color Hashed Chip Blocks")


#verification
#col_transpose_dict_decrypt = accessing_block_values.block_strands(hashed_switches, transpose_key)

#print(col_transpose_dict_decrypt)

rail_fence_transpose_dict = accessing_block_values.block_strands(hashed_switches, transpose_key)

sorted_rail_fence_transpose_dict = {i: rail_fence_transpose_dict[i] for i in transpose_key}

#print(sorted_rail_fence_transpose_dict)

ciphertext_list = list(sorted_rail_fence_transpose_dict.values())

Bob_Merkle_Root = Merkle_Tree.merkle_tree(ciphertext_list)

#color_hash_cipher = hashing.cipher_color_hashing(ciphertext_list)

#hash_verify.verify(strands_color_hash_list, color_hash_cipher)

assert Alice_Merkle_Root == Bob_Merkle_Root

# Decryption
tic = time.perf_counter()

Final_ciphertext = ''			
for i in sorted_rail_fence_transpose_dict:
	Final_ciphertext += sorted_rail_fence_transpose_dict[i]
				
#print("Rail Fence Ciphertext: " + Final_ciphertext)

#Initial_ciphertext = Columnar_Transposition.col_transpose_decryption(Final_ciphertext, transpose_key)

#print("Initial Ciphertext: " + Initial_ciphertext)

Initial_ciphertext = Rail_Fence.decryptRailFence(Final_ciphertext, transpose_key)

#print("Initial Ciphertext: " + Initial_ciphertext)

if len(Decryption_key) > len(Initial_ciphertext):
	Decryption_key = Encryption_key[0:len(Initial_ciphertext)]
	#print("Decryption key:", Decryption_key)
	decrypted_message = DNA_Vigenere.decrypt(Initial_ciphertext, Decryption_key, encoding_seq)
else:
	#print("Decryption key:", Decryption_key)
	decrypted_message = DNA_Vigenere.decrypt(Initial_ciphertext, Decryption_key, encoding_seq)

#print("Decrypted message: " + decrypted_message)

binary_list = [DNA_coding.DNA_decoding_rules[ECDH.rule][key] for num in decrypted_message for key in encoding_seq if num == key]

binary_str = "".join(binary_list)

bts = bitarray(binary_str)
ascs = bts.tobytes().decode('utf-8')

toc = time.perf_counter()
elapsed_time = toc - tic

f = open("Output_file.txt", "w")
#print('Decryption Time: ', elapsed_time, file=f)
print(ascs, file=f)
f.close()

#print("Alice's message:", ascs)
print("Decryption time:", elapsed_time)
