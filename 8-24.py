# -*- coding: utf-8 -*-
''' Знайти найбільше значення серед елементів матриці А(NxN), розміщених
	над її головною діагоналлю. Видалити стовпець, що містить заданний елемент'''

from functions.generate_matrix import generate_matrix
from functions.print_matrix import print_matrix
from functions.max_of_arr import max_of_arr


def main():
	matrix = generate_matrix(1, 10, 5, 5)
	print_matrix(matrix, text='Before\n')
	max_elements = [matrix[x-1][x] for x in range(1, len(matrix))]
	index = max_elements.index(max_of_arr(max_elements)) + 1
	for x in range(len(matrix)):
		matrix[x].pop(index)
	print_matrix(matrix, text='After:\n')
	print('\nDeleted {} column (numeration started with 0)'.format(index))
	

if __name__ == '__main__':
	main()		