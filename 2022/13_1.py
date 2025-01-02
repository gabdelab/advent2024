import ast

file = 'data/13.txt'

def is_right_order(block1, block2):
	while True:
		a = "comparing %s with %s -> " % (block1, block2)
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


if __name__ == "__main__":
	total_match = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
	pairs = data.split("\n\n")
	right_order = []
	for index, i in enumerate(pairs):
		pair1, pair2 = i.split("\n")
		# print("\n%d - %s \nvs.  %s" % (index+1, pair1, pair2))
		decision = is_right_order(ast.literal_eval(pair1), ast.literal_eval(pair2))
		if decision is True:
			# print("OK")
			right_order.append(index + 1)
		elif decision is None:
			print("ylo")
			# print("Not this time")
	print(right_order)
	print(sum(right_order))