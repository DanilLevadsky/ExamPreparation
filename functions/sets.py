def unique_list(list):
	'''analog of set() function for lists'''
	arr = []
	for elem in list:
		if elem not in arr:
			arr.append(elem)
	return arr		


def unique_char_list(string):
	'''analog of set() functions for strings
		return list of unique chars'''
	arr = []
	for char in string:
		if char not in arr:
			arr.append(char)
	return arr				