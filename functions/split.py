def split(string, pattern=' '):
	''' analog of split method'''
	array = []
	if pattern in string:
		while pattern in string:	
			index = string.find(pattern)	
			array.append(string[:index])
			if pattern in string:
				string = string[index + len(pattern):]
			if pattern not in string:
				array.append(string)	
			index = None
	else: raise Exception('Pattern did`t found')
	while '' in array:
		array.remove('')							
	return array

	