#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Доповнити матрицю рядком і стовпцем,
	в які записати суми елементів відповідних рядків
	і стовпців вихідної матриці. В елемент А(m+1)(n+1)
	записати суму всіх елементів вихідної матриці А'''

from functions.generate_matrix import * 
from functions.print_matrix import * 
from functions.sum_of_matrix import * 
from functions.add_row_and_column import * 


def main():
	min_val = int(input('minimal value in matrix: '))
	max_val = int(input('maximal value in matrix: '))
	rows = int(input('number of rows in matrix: '))
	columns = int(input('number of columns in matrix: '))
	matrix = generate_matrix(min_val, max_val, rows, columns)
	started_matrix = matrix
	print_matrix(matrix, 'Вихідна матриця')
	sum_of_columns = columns_sum(matrix)
	add_row(matrix, sum_of_columns)
	add_column(matrix)
	print_matrix(matrix, "Кінцева матриця")


if __name__ == '__main__':
	main()

