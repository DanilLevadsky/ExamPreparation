#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' У заданому рядку визначити слова, довжини яких
	співпадають із заданою користувачем'''

from functions.split import length_of_string, split


def main():
	string = input('Введіть рядок: ')	
	length = int(input('Введіть довжину: '))
	result = []
	for word in split(string):
		if length_of_string(word) == length:
			result.append(word)
	print('Результат:',' '.join(result))


if __name__ == '__main__':
	main()	