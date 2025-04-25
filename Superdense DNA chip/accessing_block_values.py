from libraries import *

def block_strands(switches, transpose_key):

	col_transpose_dict_decrypt = {}
	mismatches_dict = {}
	N = 4 # 4x4 dimension

	# accessing the hybridization points values
	hybridization_points = [switches[row][column] for row in range(N) for column in range(N) if ((row + column) == (N - 1))]

	#print(hybridization_points)

	#for i in range(len(hybridization_points)):
	#	if hybridization_points[i] != None:
	#		pairings = {transpose_key[0]:hybridization_points[i]}
	#		col_transpose_dict_decrypt.update(pairings)

	pairings = {transpose_key[0]:hybridization_points[i] for i in range(len(hybridization_points)) if hybridization_points[i] != None}
	col_transpose_dict_decrypt.update(pairings)
	
	#print(col_transpose_dict_decrypt)

	# accessing the similar base points values
	similar_base_points = [switches[row][column] for row in range(N) for column in range(N) if row == column]
	
			
	#print(similar_base_points)

	for i in range(len(similar_base_points)):
		if similar_base_points[i] != None and i%2 == 0:
			pairings = {transpose_key[3]:similar_base_points[i]}
			col_transpose_dict_decrypt.update(pairings)
		

		if similar_base_points[i] != None and i%2 == 1:
			pairings = {transpose_key[1]:similar_base_points[i]}
			col_transpose_dict_decrypt.update(pairings)
		
	#print(col_transpose_dict_decrypt)

	# Adding mismatches points values and corresponding keys in dictionary
	for row in range(N):
		for column in range(N):
			if row != column and column != N - row - 1 and switches[row][column] != None:
				if (row == 0 and column == 1) or (row == 1 and column == 0) or (row == 2 and column == 3) or (row == 3 and column == 2):
					mismatches_dict.update({transpose_key[2]: switches[row][column]})
			
				if (row == 0 and column == 2) or (row == 2 and column == 0):
					mismatches_dict.update({transpose_key[1]: switches[row][column]})
			
				if (row == 1 and column == 3) or (row == 3 and column == 1):
					mismatches_dict.update({transpose_key[3]: switches[row][column]})
			
	#print(mismatches_dict)

	# accessing the mismatch points values
	#for i in mismatches_dict.keys():
		#for j in col_transpose_dict_decrypt.keys():
			#if i != j:
				#pairings = {i:mismatches_dict[i]}
	
	pairings = {i:mismatches_dict[i] for i in mismatches_dict.keys() for j in col_transpose_dict_decrypt.keys() if i != j}
							
	col_transpose_dict_decrypt.update(pairings)
	#break			
	
	#print(col_transpose_dict_decrypt)
	
	return col_transpose_dict_decrypt
	
	
	
	
