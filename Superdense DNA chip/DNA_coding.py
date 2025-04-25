from libraries import *

DNA_encoding_rules = {1: {"00": "A", "01": "C", "10": "G","11": "T"},
                      2: {"00": "A", "01": "G", "10": "C","11": "T"},
                      3: {"00": "C", "01": "A", "10": "T","11": "G"},
                      4: {"00": "C", "01": "T", "10": "A","11": "G"},
                      5: {"00": "G", "01": "A", "10": "T","11": "C"},
                      6: {"00": "G", "01": "T", "10": "A","11": "C"},
                      7: {"00": "T", "01": "C", "10": "G","11": "A"},
                      8: {"00": "T", "01": "G", "10": "C","11": "A"}}

DNA_decoding_rules = {1: {"A": "00", "C": "01", "G": "10","T": "11"},
                      2: {"A": "00", "G": "01", "C": "10","T": "11"},
                      3: {"C": "00", "A": "01", "T": "10","G": "11"},
                      4: {"C": "00", "T": "01", "A": "10","G": "11"},
                      5: {"G": "00", "A": "01", "T": "10","C": "11"},
                      6: {"G": "00", "T": "01", "A": "10","C": "11"},
                      7: {"T": "00", "C": "01", "G": "10","A": "11"},
                      8: {"T": "00", "G": "01", "C": "10","A": "11"}}


def DNA_encoded_key(key_str):
	
	binary_list = [key_str[i: i+2] for i in range(0, len(key_str), 2)]
	
	return [DNA_encoding_rules[ECDH.rule].get(key) for num in binary_list for key in list(DNA_encoding_rules[ECDH.rule].keys()) if num == key]

def DNA_encoded_message(content):
	
	DNA_list = []
	for x in bytearray(content, 'utf-8'):
		binary_str = ''.join(format(x, '08b'))
		binary_list = [binary_str[i: i+2] for i in range(0, len(binary_str), 2)]
		for num in binary_list:
			for key in list(DNA_encoding_rules[ECDH.rule].keys()):
				if num == key:
					DNA_list.append(DNA_encoding_rules[ECDH.rule].get(key))
		
	return DNA_list	
	
