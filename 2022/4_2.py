from itertools import zip_longest

file = 'data/4.txt'

def overlaps(start_a, end_a, start_b, end_b):
	"""Returns true if there is an overlap between a and b"""
	return int(start_a) <= int(end_b) and int(end_a) >= int(start_b)

if __name__ == "__main__":
	total_match = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
		for i in data.split("\n"):
			a, b = i.split(",")[:2]
			start_a, end_a = a.split("-")[:2]
			start_b, end_b = b.split("-")[:2]
			if overlaps(start_a, end_a, start_b, end_b) \
				or overlaps(start_b, end_b, start_a, end_a):
				total_match += 1
				print("OK: %s %s" % (a, b))
			else:
				print("no overlap: %s %s" % (a, b))
			print(total_match)

