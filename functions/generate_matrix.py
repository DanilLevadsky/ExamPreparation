from random import randint

def generate_matrix(min_val, max_val, rows, columns):
	return [[randint(min_val, max_val) for x in range(columns)] for y in range(rows)]
