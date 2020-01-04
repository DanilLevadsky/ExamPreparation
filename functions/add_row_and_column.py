'''функции для лабораторной работы 8-1'''
from . import sum_of_arr 

def add_column(matrix):
	for arr in matrix:
		arr.append(sum_of_arr.sum_of_arr(arr))
	return matrix


def columns_sum(matrix):
	arr = []
	for column in range(len(matrix[0])):
		sum = 0
		for row in matrix:
			sum += row[column]
		arr.append(sum)	
	return arr	


def add_row(matrix, arr):
	return matrix.append(arr)		