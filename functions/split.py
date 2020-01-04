def split(string, pattern=' '):
	''' analog of split method'''
	array = []
	for s in string:
		if s == pattern:
			array.append(string[:string.index(s)])
			string = string[(string.index(s) + 1):]
			if string.count(pattern) == 0  and len(string) > 0:
				array.append(string)	
	for elem in array:
		if elem == '':
			array.remove(elem)			
	return array
