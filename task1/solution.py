def solution(number):
	string = '1'
	index = 1
	if number == 1: return 1
	if number < 0 or number == 2 or number == 4 or number == 5: return 'Incorrect number'
	if (number - 1) % 5 == 0:
		temp = int((number - 1) // 5)
		return ('('*temp) + string + ('+5)'*temp)
	else:
		while number != 1:
			if (number % 3) == 0:
				number /= 3
				string = "(" + string[:index] + "*3)" + string[index:]
				index += 1
			else:	
				number -= 5
				string = '(' + string[:index] + '+5)' + string[index:]
				index += 1
	return string			 		


def main():
	number = int(input('Enter number: '))
	print(solution(number))


if __name__ == '__main__':
	main()