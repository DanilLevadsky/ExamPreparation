def print_matrix(matrix, text=''):
	print(text)
	for row in matrix:
		for elem in row:
			print('{:5}'.format(elem), end='')
		print()
	print()		
