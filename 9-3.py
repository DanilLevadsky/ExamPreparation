#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Заданий рядок, що містить розділені пробілами слова
	відсортувати слова за зростанням їх довжини'''

from functions.split import split


def main():
	string = input('Введіть рядок: ')
	arr = split(string)
	arr.sort(key=len)
	result = ' '.join(arr)
	print(result)
	

if __name__ == '__main__':
	main()		