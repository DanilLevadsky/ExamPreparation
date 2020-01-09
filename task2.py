''' взять матрицу произвольную разделить на 4 ровные части и покрутить 
	эти части 3 раза против часовой стрелки меняя их местами'''

from functions.print_matrix import print_matrix
from functions.generate_matrix import generate_matrix
from functions.zero_matrix import zero_matrix


def rotate_matrix(matrix, dimension):
	new_matrix = zero_matrix(dimension, dimension)
	for x in range(len(matrix)):
		for y in range(len(matrix)):
			new_matrix[x][y] = matrix[y][::-1][x]
	matrix = new_matrix
	return matrix
	

def cut_matrix(matrix):
	centre = len(matrix) // 2
	result = [[] for x in range(4)]
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if i > centre -1:
				if j > centre -1:
					result[3].append(matrix[i][j])
				else: 
					result[2].append(matrix[i][j])
			else:
				if j > centre -1:
					result[1].append(matrix[i][j])
				else:
					result[0].append(matrix[i][j])			
	return result
		

def create_matrix(arr, dimension):
	matrix = [[] for x in range(dimension)]
	j = 0
	for i in range(len(arr)):
		if i % dimension == 0 and i != 0:
			j += 1
		matrix[j].append(arr[i])	
	return matrix	


def main():
	dimension = int(input('Dimension: '))
	matrix = generate_matrix(1, 10, dimension, dimension)
	print_matrix(matrix)
	squares = cut_matrix(matrix)
	matr_arr = [create_matrix(x, dimension//2) for x in squares]
	matr = None
	for y in range(len(matr_arr)):
		for x in range(4):	
			if x == 0:
				matr = 	matr_arr[y]
				print_matrix(matr, text='Square №{} before rotation'.format(y+1))
			else:	
				matr = rotate_matrix(matr, dimension//2)
				print_matrix(matr, text='Square №{} after rotation №{}'.format(y+1, x))
		print('\n')		



if __name__ == '__main__':
	main()	