def split(string, pattern=' '):
	arr = []
	for s in string:
		if s == pattern:
			arr.append(string[:string.index(s)])
			string = string[(string.index(s) + 1):]
			if string[-1] != pattern and string.count(pattern) == 0:
				arr.append(string)	
	return arr
