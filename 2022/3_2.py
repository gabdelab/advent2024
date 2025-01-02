from itertools import zip_longest

file = 'data/3.txt'


def grouper(n, iterable, fillvalue=None):
	args = [iter(iterable)] * n
	return zip_longest(fillvalue=fillvalue, *args)

def points_from_letter(letter):
	if letter.isupper():
		return ord(letter) - 38
	else:
		return ord(letter) - 96

if __name__ == "__main__":
	total_points = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
		for i1, i2, i3 in grouper(3, data.split("\n")):
			print("%s - %s - %s" % (i1, i2, i3))

			common = list(set(i1).intersection(set(i2)).intersection(set(i3)))[0]
			total_points += points_from_letter(common)
			print("%s - %s" % (common, total_points))