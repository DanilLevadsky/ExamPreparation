#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' У заданому рядку підрахувати кількість слів, 
	які починаються групою заданих слів'''

from functions.split import length_of_string, split


def main():
	string = input('Введіть рядок: ')
	pattern = input('Введіть символи, на які починаються слова: ')
	result = []
	for word in split(string):
		if word[:(length_of_string(pattern))] == pattern:
			result.append(word)
	print("Такі слова:", ' '.join(result))


if __name__ == '__main__':
	main()			