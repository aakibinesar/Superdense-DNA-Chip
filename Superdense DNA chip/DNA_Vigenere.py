from libraries import *

# This function takes the first key string (the "top" key) and then create the top line of our matrix which starts off
# with the key and then ends using all remaining letters of the alphabet. It is required that the key only use
# each letter of the alphabet once.
def createAlphabet(encoding_rule):

    alphabet = ['A','C','G','T']
    topAlphabet = alphabet
    counter = 0

    for letter in encoding_rule:

        topAlphabet.remove(letter)

        topAlphabet.insert(counter, letter)

        counter += 1
        
    return topAlphabet
    
# This function takes the second key and creates each new line "underneath" the previous one, it also modulos through
# the the alphabet created by the createAlphabet function starting with the each letter in the string.
def createLines(encoding_rule, myAlphabet):

    listOfAlphabets = []

    for letter in encoding_rule:

        index = myAlphabet.index(letter)

        counter = 0

        lineAlphabet = []

        while counter <= 3:
            lineAlphabet.append(myAlphabet[index % len(myAlphabet)])
            index += 1
            counter += 1

        listOfAlphabets.append(lineAlphabet)

    return listOfAlphabets

# DNA Vigenere Encryption
def encrypt(message, key, alphabet):
    
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
    
    switches = [[None for _ in range(len(letter_to_index))] for _ in range(len(letter_to_index))]
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            switches[letter_to_index[letter]][letter_to_index[key[i]]] = index_to_letter[number] 
            encrypted += index_to_letter[number]
            i += 1
    	
    return encrypted, switches


# DNA Vigenere Decryption
def decrypt(cipher, key, alphabet):
    
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))	

    Decryption_key = str(key)

    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted
    
