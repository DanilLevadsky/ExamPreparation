def split(string, pattern=' '):
	''' analog of split method'''
	array = []
	if pattern in string:
		if len(pattern) == 1:	
			for s in string:
				if s == pattern:
					array.append(string[:string.index(s)])
					string = string[(string.index(s) + 1):]
					if string.count(pattern) == 0  and len(string) > 0:
						array.append(string)	
			for elem in array:
				if elem == '':
					array.remove(elem)
		elif len(pattern) > 1:
			while pattern in string:	
				index = string.find(pattern)
				array.append(string[:index])
				if pattern in string:
					string = string[index + len(pattern):]
				if pattern not in string:
					array.append(string)	
				index = None
	else: raise Exception('Pattern did`t found')
	for elem in array:
		if elem == '':
			array.remove(elem)							
	return array