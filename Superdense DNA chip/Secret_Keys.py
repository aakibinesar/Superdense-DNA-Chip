from libraries import *

# Remove n leading zeroes from binary number 
def remove_leading_zeroes(binary_number, n): 
    binary_number = binary_number[n:] 
    return binary_number 
 
# Add n leading zeroes to binary number 
def add_leading_zeroes(binary_number, n): 
    binary_number = "0"*n + binary_number 
    return binary_number

#generating DNA encoded key

def encryption_key(key):
	
	print("Length of initial shared key in bits:",(len(key)))
	if len(key) == 256:
		
		DNA_encoded_key = ''.join(DNA_coding.DNA_encoded_key(key))
	
		#print(DNA_encoded_key)
		#print(len(DNA_encoded_key))
	
	elif len(key) < 256:
	
		n = 256 - len(key)
	
		key = add_leading_zeroes(key, n)
			
		DNA_encoded_key = ''.join(DNA_coding.DNA_encoded_key(key))
	
		#print(DNA_encoded_key)
		#print(len(DNA_encoded_key))

	elif len(key) > 256:
	
		n = len(key) - 256
	
		key = remove_leading_zeroes(key, n)
			
		DNA_encoded_key = ''.join(DNA_coding.DNA_encoded_key(key))
	
		#print(DNA_encoded_key)
		#print(len(DNA_encoded_key))


	DNA_key = Seq(DNA_encoded_key)
	Encryption_key = str(DNA_key.reverse_complement())
		
	return Encryption_key	
		
def decryption_key(key):
	
	print("Length of initial shared key in bits:",(len(key)))
	if len(key) == 256:
		
		DNA_encoded_key = ''.join(DNA_coding.DNA_encoded_key(key))
	
		#print(DNA_encoded_key)
		#print(len(DNA_encoded_key))
	
	elif len(key) < 256:
	
		n = 256 - len(key)
	
		key = add_leading_zeroes(key, n)
			
		DNA_encoded_key = ''.join(DNA_coding.DNA_encoded_key(key))
	
		#print(DNA_encoded_key)
		#print(len(DNA_encoded_key))

	elif len(key) > 256:
	
		n = len(key) - 256
	
		key = remove_leading_zeroes(key, n)
			
		DNA_encoded_key = ''.join(DNA_coding.DNA_encoded_key(key))
	
		#print(DNA_encoded_key)
		#print(len(DNA_encoded_key))


	DNA_key = Seq(DNA_encoded_key)
	Decryption_key = str(DNA_key.reverse_complement())
		
	return Decryption_key		
		
		
