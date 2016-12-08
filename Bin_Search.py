def bin_search():
	n = int(raw_input("Enter a number as the end point of an array:"))
	array = range(1, n + 1)
	min = 1
	max = n - 1
	target = int(raw_input("Enter target:"))
	status = "not found"
	while status == "not found":
		guess = (min + max) / 2
		if array[guess] == target:
			status = "found"
			print target, "is at index", guess
			return guess
		else:
			if array[guess] < target:
				min = guess + 1
				if min > max: 
					print target, "is not in array."
					break
			else:
				max = guess - 1
				if max < min:
					print target, "is not in array."
					break

bin_search()