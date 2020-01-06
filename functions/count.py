def count(array, item):
	counter = 0
	for elem in array:
		if elem == item:
			counter += 1
	return counter