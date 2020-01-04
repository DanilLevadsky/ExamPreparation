#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' У заданому рядку символів визначити кількість слів,
	довжина яких більша за вказану користувачем'''

from functions.split import split

def main():
	length = int(input('Введіть довжину: '))
	string = input('Введіть строку: ')
	count = 0
	for word in split(string):
		if len(word) > length:
			count += 1
	print('кількість слів:', count)		

if __name__ == '__main__':
	main()	