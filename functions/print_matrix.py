def print_matrix(matrix, text=''):
	print(text)
	for x in matrix:
		for y in x:
			print('{:5}'.format(y), end='')
		print()
	print()		