file = 'data/3.txt'


if __name__ == "__main__":
	total_points = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
		for i in data.split("\n"):
			half = int(len(i)/2)
			start = i[:half]
			end = i[half:]
			common = list(set(start).intersection(set(end)))[0]
			if common.isupper():
				total_points += ord(common) - 38
			else:
				total_points += ord(common) - 96
			print("%s - %s" % (common, total_points))