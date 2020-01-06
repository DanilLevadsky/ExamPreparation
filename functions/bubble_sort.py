def bubble_sort(arr, reverse=False):
	'''bubble-sort'''
	swapped = True
	while swapped:
		swapped = False
		for x in range(len(arr) -1):
			if arr[x] > arr[x + 1]:
				arr[x], arr[x + 1] = arr[x + 1], arr[x]
				swapped = True
	if reverse == True: return arr[::-1]
	else: return arr