import importlib

file = 'data/11_ex.txt'


def do_operation(monkey, worry):
	# If we modulo by 6 * 19 * 23 * 13 * 17 it should be ok
	worry = worry % (19 * 23 * 13 * 17)
	if monkey == 0:
		return int((worry * 19) / 1) # TODO changeme
	if monkey == 1:
		return int((worry + 6) / 1)
	if monkey == 2:
		return int((worry * worry) / 1)
	if monkey == 3:
		return int((worry + 3) / 1)


def test_and_give(monkey, worry):
	if monkey == 0:
		if worry % 23 == 0:
			return 2
		else:
			return 3
	if monkey == 1:
		if worry % 19 == 0:
			return 2
		else:
			return 0
	if monkey == 2:
		if worry % 13 == 0:
			return 1
		else:
			return 3
	if monkey == 3:
		if worry % 17 == 0:
			return 0
		else:
			return 1

if __name__ == "__main__":
	initial = {
		0: [79, 98],
		1: [54, 65, 75, 74],
		2: [79, 60, 97],
		3: [74]
	}
	inspections = {0: 0, 1:0, 2:0, 3:0}
	for _ in range(10000):
		for monkey in range(4):
			inspections[monkey] += len(initial[monkey])
			for index, element in enumerate(initial[monkey]):
				worry = do_operation(monkey, element)
				out_monkey = test_and_give(monkey, worry)
				initial[out_monkey].append(worry)
				print("%s - %s - %s - %s" % (element, worry, out_monkey, initial))
			initial[monkey] = []
	print(initial)
	print(inspections)