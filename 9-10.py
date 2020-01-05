#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' У заданому рядку символів визначити символи, які зустрічаються
	по одному разу і надрукувати номери їх позицій'''


def main():
	string = input('Введите строку символов: ')
	for char in string:
		if string.count(char) == 1:
			print(char, '––', string.index(char))

if __name__ == '__main__':
	main()