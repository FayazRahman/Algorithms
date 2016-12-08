array = map(int, raw_input("Type in a few numbers:").split())

def selection_sort(array):
	for i in range(len(array)):
		mini = min(array[i:]) #Find minimum
		idx_min = array[i:].index(mini) #Find index of minimum
		array[i + idx_min] = array[i] #Replace element at idx_min with the first element
		array[i] = mini #Replace first element with mini
	print array
	return array

selection_sort(array)