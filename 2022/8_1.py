from collections import defaultdict

file = 'data/8.txt'
size = 99

def is_tallest(mylist, element):
	return all(element > i for i in mylist)

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()

	rows = {}
	columns = defaultdict(list)

	results = []
	for index, row in enumerate(data.split("\n")):
		if row == "":
			continue
		rows[index+1] = [r for r in row]
		for index, char in enumerate(row):
			columns[index+1].append(char)

	for row_index in range(1, size+1):
		for column_index in range(1, size+1):
			row = rows[row_index]
			column = columns[column_index]
			if row[column_index-1] != column[row_index-1]:
				raise ValueError("invalid model: %s %s" % (column_index, row_index))
			element = row[column_index-1]

			if is_tallest(column[:row_index-1], element) \
				or is_tallest(column[row_index:], element) \
				or is_tallest(row[:column_index-1], element) \
				or is_tallest(row[column_index:], element):
				results.append(element)
	print(len(results))