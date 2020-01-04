def split(string, pattern=' '):
	''' analog of split method'''
	array = []
	for s in string:
		if s == pattern:
			array.append(string[:string.index(s)])
			string = string[(string.index(s) + 1):]
			if string.count(pattern) == 0:
				array.append(string)	
	return array
