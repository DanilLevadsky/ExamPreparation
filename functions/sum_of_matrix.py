def sum_of_matrix(matrix):
	sum = 0
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			sum += y
	return sum		