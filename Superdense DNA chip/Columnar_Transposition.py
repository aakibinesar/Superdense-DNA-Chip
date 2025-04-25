from libraries import *
	
def col_transpose_encryption(s,k):

    b=math.ceil(len(s)/len(k))

    arr=[['' for i in range(len(k))]
         for j in range(b)]
    i=0
    j=0
    # arranging the message into matrix
    for h in range(len(s)):
        arr[i][j]=s[h]
        j+=1
        if(j>len(k)-1):
            j=0
            i+=1
    #print("The message matrix is: ")
    #for i in arr:
        #print(i)
    
    	

    cipher_text=""
    transpose_dict = {}
    # To get indices as the key numbers instead of alphabets in the key, according
    # to algorithm, for appending the elementsof matrix formed earlier, column wise.
    kk=sorted(k)

    for i in kk:
        probe = ""
        # gives the column index
        h=k.index(i)
        for j in range(len(arr)):
            cipher_text+=arr[j][h]
            probe += arr[j][h]
        pairings = {k[h]:probe}
        transpose_dict.update(pairings)
        #print(probe)
                
    return cipher_text, transpose_dict
    
    
def col_transpose_decryption(s,k):

    b=math.ceil(len(s)/len(k))

    arr=[['' for i in range(len(k))]
         for j in range(b)]

    # To get indices as the key numbers instead of alphabets in the key, according
    # to algorithm, for appending the elementsof matrix formed earlier, column wise.
    kk=sorted(k)

    d=0
    # arranging the cipher message into matrix
    # to get the same matrix as in encryption
    for i in kk:
        h=k.index(i)
        for j in range(len(arr)):
            arr[j][h]=s[d]
            d+=1

    #print("The message matrix is: ")
    #for i in arr:
        #print(i)

    # the plain text
    plain_text=""
    for i in arr:
        for j in i:
            plain_text+=j

    return plain_text
