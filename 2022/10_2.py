file = 'data/10.txt'

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()
	counter = 1
	register = 1
	total = 0
	draw = ""

	for x, i in enumerate(data.split("\n")):
		previous_counter = counter
		previous_register = register
		if i == "":
			continue
		# if abs(previous_counter %40 - register) <= 1:
		# 	draw += "#"
		# else:
		# 	draw += "."
		if i[:4] == "noop":
			if abs((counter-1) %40 - register) <= 1:
				print("e - " + str(register) + " - " + str(counter) + " ( " + str(counter%40)+ " )")
				draw += "#"
			else:
				draw += "."
				print("f - " + str(register) + " - " + str(counter) + " ( " + str(counter%40)+ " )")
			counter += 1
		else:
			if abs((counter-1) %40 - register) <= 1:
				print("a - " + str(register) + " - " + str(counter) + " ( " + str(counter%40)+ " )")
				draw += "#"
			else:
				print("b - " + str(register) + " - " + str(counter) + " ( " + str(counter%40)+ " )")
				draw += "."
			counter += 1
			if abs((counter-1) %40 - register) <= 1:
				print("c - " + str(register) + " - " + str(counter) + " ( " + str(counter%40)+ " )")
				draw += "#"
			else:
				print("d - " + str(register) + " - " + str(counter) + " ( " + str(counter%40)+ " )")
				draw += "."
			counter += 1
			register += int(i[5:])
			#draw += "."

	print(draw[:40])
	print(draw[40:80])
	print(draw[80:120])
	print(draw[120:160])
	print(draw[160:200])
	print(draw[200:240])
