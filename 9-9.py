#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' ввести рядок символів, переформатувавши його, подовживши
	до довжини 60 символів рівномірним додаванням пробілів між
	словами. Визначити кількість доданих пробілів'''

from functions.split import split, string_to_char_list, length_of_arr

def main():
	string = input('Введіть рядок: ')
	print('Відформатований рядок:', add_spaces(string))


def add_spaces(string):
	string_array = string_to_char_list(string)
	i = 0
	while True:
		if length_of_arr(string_array) == 60:
			break
		if i == length_of_arr(string_array) - 1:
			i = 0
		if string_array[i] == ' ':
			string_array.insert(i, ' ')
			i += 2			
		i += 1
	return ''.join(string_array)		


if __name__ == '__main__':
	main()		