import importlib

file = 'data/11.txt'


def do_operation(monkey, worry):
	worry = worry % (17*3*5*7*11*19*2*13)

	if monkey == 0:
		return int((worry * 7) / 1) # TODO changeme
	if monkey == 1:
		return int((worry + 4) / 1)
	if monkey == 2:
		return int((worry + 2) / 1)
	if monkey == 3:
		return int((worry + 7) / 1)
	if monkey == 4:
		return int((worry * 17) / 1)
	if monkey == 5:
		return int((worry + 8) / 1)
	if monkey == 6:
		return int((worry + 6) / 1)
	if monkey == 7:
		return int((worry * worry) / 1)


def test_and_give(monkey, worry):
	if monkey == 0:
		return 5 if worry % 17 == 0 else 3
	if monkey == 1:
		return 0 if worry % 3 == 0 else 3
	if monkey == 2:
		return 7 if worry % 5 == 0 else 4
	if monkey == 3:
		return 5 if worry % 7 == 0 else 2
	if monkey == 4:
		return 1 if worry % 11 == 0 else 6
	if monkey == 5:
		return 2 if worry % 19 == 0 else 7
	if monkey == 6:
		return 0 if worry % 2 == 0 else 1
	if monkey == 7:
		return 6 if worry % 13 == 0 else 4

if __name__ == "__main__":
	initial = {
		0: [54, 89, 94],
		1: [66, 71],
		2: [76, 55, 80, 55, 55, 96, 78],
		3: [93, 69, 76, 66, 89, 54, 59, 94],
		4: [80, 54, 58, 75, 99],
		5: [69, 70, 85, 83],
		6: [89],
		7: [62, 80, 58, 57, 93, 56],
	}
	inspections = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
	for _ in range(10000):
		for monkey in range(8):
			inspections[monkey] += len(initial[monkey])
			for index, element in enumerate(initial[monkey]):
				worry = do_operation(monkey, element)
				out_monkey = test_and_give(monkey, worry)
				initial[out_monkey].append(worry)
				# print("%s - %s - %s - %s" % (element, worry, out_monkey, initial))
			initial[monkey] = []
	print(initial)
	print(inspections)