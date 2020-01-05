from sets import unique_char_list 

def string_isdigit(string):
	''' analog of isdigit(), checks if
		the string consists only of digits'''
	digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	if all([char in digits for char in unique_char_list(string)]):
		return True
	else: return False	

def string_isalpha(string):
	''' analog of isalpha(), checks if the
		string consists only of letters'''
	chars = unique_char_list(string)
	if all([('a' <= char.lower() <= 'z') or ('а' <= char.lower() <= 'я') for char in chars]):
		return True
	else: return False	
