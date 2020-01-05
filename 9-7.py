#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Із заданого рядка вилучити слова, довжина яких
	менша за вказану користувачем'''

from functions.split import split, length_of_string


def main():
	string = input('Введіть рядок: ')
	length = int(input('Введіть довжину: '))
	arr = split(string)
	result = [x for x in arr if length_of_string(x) > length]
	print('Результат:', ' '.join(result))


if __name__ == '__main__':
	main()	