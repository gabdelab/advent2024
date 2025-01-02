from collections import defaultdict

file = 'data/8.txt'
size = 99

def get_score(mylist, element):
	if mylist == []:
		return 0
	if mylist[0] >= element:
		return 1
	return 1 + get_score(mylist[1:], element)

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()

	rows = {}
	columns = defaultdict(list)

	for index, row in enumerate(data.split("\n")):
		if row == "":
			continue
		rows[index+1] = [r for r in row]
		for index, char in enumerate(row):
			columns[index+1].append(char)

	best_score = 0
	for row_index in range(1, size+1):
		for column_index in range(1, size+1):
			row = rows[row_index]
			column = columns[column_index]
			if row[column_index-1] != column[row_index-1]:
				raise ValueError("invalid model: %s %s" % (column_index, row_index))
			element = row[column_index-1]

			score = get_score(list(reversed(column[:row_index-1])), element) \
				*get_score(column[row_index:], element)\
				*get_score(list(reversed(row[:column_index-1])), element)\
				*get_score(row[column_index:], element)
			if score > best_score:
				best_score = score
				print(row_index, column_index)
	print(best_score)