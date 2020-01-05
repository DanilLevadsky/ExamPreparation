#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' У заданому рядку символів визначити кількість слів,
	у яких співпадають перший та останній символи'''

from functions.split import split, length_of_arr


def main():
	string = input('Введіть рядок: ')
	words = split(string)
	result = [x for x in words if x[0] == x[-1]]
	print('Такі слова: ', ' '.join(result))
	print('Їхня кількість: ', length_of_arr(result))


if __name__ == '__main__':
	main()	