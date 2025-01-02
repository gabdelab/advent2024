import re


file = 'data/16_ex.txt'

if __name__ == "__main__":
	pattern = re.compile(r"""(?P<name>)""", re.VERBOSE)
	with open(file, 'r') as open_file:
		data = open_file.read()
	for row in data.split("\n"):
		match = pattern.match(row)	
		print(match.group("name"))