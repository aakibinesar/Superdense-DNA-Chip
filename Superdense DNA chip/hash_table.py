from libraries import *

#black = '#000000'
#yellow = '#FFFF00'
#red = '#FF0000'
#green = '#00FF00'
#orange = '#FFA500'

def hashed_dict(switches, encoding_seq):

	if switches[0][0] == None or switches[2][2] == None:
	
		switches[0][0] = None
		switches[2][2] = None
		
		hash_dic = {}
		hash_table = {0:'#FFA500', 1:'#FF0000', 2:'#FFA500', 3:'#FFFF00'}
		
		#for i in encoding_seq:
		#	for key, value in hash_table.items():
		#		if encoding_seq.index(i) == key:
		#			hash_dic.update({str(i):value})
		
		dic = {str(i):value for i in encoding_seq for key, value in hash_table.items() if encoding_seq.index(i) == key}
		
		hash_dic.update(dic)
			
		return hash_dic, switches
		

	elif switches[1][1] == None or switches[3][3] == None or switches[1][3] == None or switches[3][1] == None:
		
		switches[1][1] = None
		switches[3][3] = None
		switches[1][3] = None
		switches[3][1] = None
		
		hash_dic = {}
		hash_table = {0:'#00FF00', 1:'#FF0000', 2:'#FFA500', 3:'#FFFF00'}
		
		#for i in encoding_seq:
		#	for key, value in hash_table.items():
		#		if encoding_seq.index(i) == key:
		#			hash_dic.update({str(i):value})
		
		dic = {str(i):value for i in encoding_seq for key, value in hash_table.items() if encoding_seq.index(i) == key}
		
		hash_dic.update(dic)
			
		return hash_dic, switches

	else:
		switches[1][1] = None
		switches[3][3] = None
		switches[1][3] = None
		switches[3][1] = None
		
		hash_dic = {}
		hash_table = {0:'#00FF00', 1:'#FF0000', 2:'#FFA500', 3:'#FFFF00'} 
		
		#for i in encoding_seq:
		#	for key, value in hash_table.items():
		#		if encoding_seq.index(i) == key:
		#			hash_dic.update({str(i):value})
		
		dic = {str(i):value for i in encoding_seq for key, value in hash_table.items() if encoding_seq.index(i) == key}
		
		hash_dic.update(dic)
			
		return hash_dic, switches
		
		

