def min_of_arr(arr):
	min = None
	for x in arr:
		if min == None or x < min:
			min = x
	return min