#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Ввести 2 рядки. Вилучити з першого рядка всі слова,
	які зустрічаються у другому рядку'''

from functions.split import split

def main():
	string1 = input('Перший рядок: ')	
	string2 = input('Другий рядок: ')
	arr1 = split(string1)	
	arr2 = split(string2)
	print('Результат:', ' '.join([x for x in arr1 if x not in arr2]))
	

if __name__ == '__main__':
	main()				