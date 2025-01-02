file = 'data/10.txt'

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()
	counter = 1
	register = 1
	total = 0
	for x, i in enumerate(data.split("\n")):
		previous_counter = counter
		previous_register = register
		if i == "":
			continue
		if i[:4] == "noop":
			counter += 1
		else:
			counter += 2
			register += int(i[5:])

		if previous_counter <= 20 and counter > 20:
			print("%s) %s / %d -> %d - %d (%d)" % (x+1, i, previous_counter, counter, previous_register, register))
			total += previous_register * 20
		if previous_counter <= 60 and counter > 60:
			print("%s) %s / %d -> %d - %d (%d)" % (x+1, i, previous_counter, counter, previous_register, register))
			total += previous_register * 60
		if previous_counter <= 100 and counter > 100:
			print("%s) %s / %d -> %d - %d (%d)" % (x+1, i, previous_counter, counter, previous_register, register))
			total += previous_register * 100
		if previous_counter <= 140 and counter > 140:
			print("%s) %s / %d -> %d - %d (%d)" % (x+1, i, previous_counter, counter, previous_register, register))
			total += previous_register * 140
		if previous_counter <= 180 and counter > 180:
			print("%s) %s / %d -> %d - %d (%d)" % (x+1, i, previous_counter, counter, previous_register, register))
			total += previous_register * 180
		if previous_counter <= 220 and counter > 220:
			print("%s) %s / %d -> %d - %d (%d)" % (x+1, i, previous_counter, counter, previous_register, register))
			total += previous_register * 220
	print(total)