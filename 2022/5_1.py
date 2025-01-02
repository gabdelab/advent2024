file = 'data/5.txt'

if __name__ == "__main__":
	total_match = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
	initial, moves = data.split("\n\n")[:2]

	# Initials looks like this
	# [P]     [C]         [M]
	# [D]     [P] [B]     [V] [S]
	# [Q] [V] [R] [V]     [G] [B]
	# [R] [W] [G] [J]     [T] [M]     [V]
	# [V] [Q] [Q] [F] [C] [N] [V]     [W]
	# [B] [Z] [Z] [H] [L] [P] [L] [J] [N]
	# [H] [D] [L] [D] [W] [R] [R] [P] [C]
	# [F] [L] [H] [R] [Z] [J] [J] [D] [D]
	#  1   2   3   4   5   6   7   8   9

	# We are hard-coding the translation
	initial = {
		"1": ["F", "H", "B", "V", "R", "Q", "D", "P"], 
		"2": ["L", "D", "Z", "Q", "W", "V"],
		"3": ["H", "L", "Z", "Q", "G", "R", "P", "C"],
		"4": ["R", "D", "H", "F", "J", "V", "B"],
		"5": ["Z", "W", "L", "C"],
		"6": ["J", "R", "P", "N", "T", "G", "V", "M"],
		"7": ["J", "R", "L", "V", "M", "B", "S"],
		"8": ["D", "P", "J"],
		"9": ["D", "C", "N", "W", "V"]
	}

	for i in moves.split("\n"):
		print(i)
		a, b, c = i.split(" ")[1::2][:3]
		for i in range(int(a)):
			# Move as many blocks as a is big, from b to c
			to_move = initial[b][-1]
			initial[b] = initial[b][:-1]
			initial[c].append(to_move)

			print(initial)