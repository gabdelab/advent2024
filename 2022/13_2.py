import ast

file = 'data/13.txt'

def is_right_order(block1, block2):
	while True:
		# a = "comparing %s with %s -> " % (block1, block2)
		if len(block1) == 0 and len(block2) == 0:
			return None
		if len(block1) == 0:
			return True
		if len(block2) == 0:
			return False
		item1 = block1[0]
		item2 = block2[0]
		block1 = block1[1:]
		block2 = block2[1:]

		if isinstance(item1, int) and isinstance(item2, int):
			if item1 == item2:
				continue
			if item1 < item2:
				return True
			else:
				return False
		elif isinstance(item1, list) and isinstance(item2, list):
			b = is_right_order(item1, item2)
			if b is None:
				continue
			elif b is True:
				return True
			else:
				return False
		elif isinstance(item1, int) and isinstance(item2, list):
			b = is_right_order([item1], item2)
			if b is None:
				continue
			elif b is True:
				return True
			else:
				return False
		elif isinstance(item1, list) and isinstance(item2, int):

			b= is_right_order(item1, [item2])
			if b is None:
				continue
			elif b is True:
				return True
			else:
				return False

def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if is_right_order(x, pivot):
                less.append(x)
            else:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def bubblesort(unsorted_list):   
    for i in range(0,len(unsorted_list)-1):  
        for j in range(len(unsorted_list)-1):  
            if(is_right_order(unsorted_list[j+1], unsorted_list[j])):  
                temp_storage = unsorted_list[j]  
                unsorted_list[j] = unsorted_list[j+1]  
                unsorted_list[j+1] = temp_storage  
    return unsorted_list  

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()
	pairs = []
	pairs_incl_empty = data.split("\n")
	for i in pairs_incl_empty:
		if i:
			pairs.append(ast.literal_eval(i))
	pairs.append([[2]])
	pairs.append([[6]])
	i_am_sorted = bubblesort(pairs)
	for i,j in enumerate(i_am_sorted):
		if j == [[2]] or j == [[6]]:
			print(i+1)
