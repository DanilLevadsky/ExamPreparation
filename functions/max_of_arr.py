def max_of_arr(arr):
	max = None
	for x in arr:
		if max == None or max < x:
			max = x
	return max		
