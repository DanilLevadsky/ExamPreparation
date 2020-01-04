#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' заданий рядок символів, що містить цифри і пробіли
	групи цифр, що розділені пробілами вважаємо словом
	розглядаючи кожне слово як число, знайти їх суму'''

from functions.split import split


def main():
	sum = 0
	string = input('Введіть рядок: ')
	arr = split(string)
	for word in arr:
		sum += int(word)
	print("Сума:", sum)


if __name__ == '__main__':
	main()			