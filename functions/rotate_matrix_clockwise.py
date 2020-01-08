def rotate_matrix_clockwise(matrix, dimension):
	new_matrix = zero_matrix(dimension, dimension)
	for x in range(1, len(matrix)+1):
		for y in range(len(matrix)):
			new_matrix[x-1][-y] = matrix[y-1][x-1]
	return new_matrix