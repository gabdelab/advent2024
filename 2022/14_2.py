file = 'data/14.txt'
HEIGHT = 193

# file = 'data/14_ex.txt'
# HEIGHT = 13


POURER = 500
WIDTH = 400
DRAW = "\n".join(["".join(["." for j in range(WIDTH)]) for i in range(HEIGHT)])


def get_destination(myDraw):
	current_index = int((WIDTH/2)-1)
	initial = current_index
	while True:
		# if myDraw[current_index-1] == "X":
		# 	return myDraw
		if current_index > WIDTH * HEIGHT:
			return None
		if myDraw[current_index+WIDTH+1] in ["X", "#"]:
			# First go left
			if myDraw[current_index+WIDTH] in ["X", "#"]:
				# Then, right
				if myDraw[current_index+WIDTH+2] in ["X", "#"]:
					# If none of these positions is OK we draw current_index
					
					myDraw = myDraw[:current_index] + "X" + myDraw[current_index+1:]
					if current_index == initial:
						return "yolo"
					return myDraw
				else:
					current_index += WIDTH+2
					continue
			else:
				current_index += WIDTH
				continue
		else:
			current_index += WIDTH+1
			continue



	# Return the height and width where the next sand will fall.
	# If none, it will return None
	return POURER

def count_sand(DRAW):
	counter = 0
	draw = DRAW
	while draw is not None:
		a = get_destination(draw)
		counter += 1
		if a == "yolo":
			return counter
		draw = a

	return counter

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()	

	max_row = 0
	for row in data.split("\n"):
		previous_i, previous_j = None, None
		for position in row.split(" -> "):
			i, j = position.split(",")[:2]
			i, j = int(i), int(j)
			max_row = max(j, max_row)
			if previous_i and previous_j:
				print(previous_i, previous_j, i, j)
				if previous_i == i:
					for path in range(j, previous_j + 1):
						index = int(path*(WIDTH+1)+i-POURER+(WIDTH/2))
						DRAW = DRAW[:index-1] + "#" + DRAW[index:]
					for path in range(previous_j, j + 1):
						index = int(path*(WIDTH+1)+i-POURER+(WIDTH/2))
						DRAW = DRAW[:index-1] + "#" + DRAW[index:]
				elif previous_j == j:
					for path in range(i, previous_i + 1):
						index = int(j*(WIDTH+1)+path-POURER+(WIDTH/2))
						DRAW = DRAW[:index-1] + "#" + DRAW[index:]
					for path in range(previous_i, i + 1):
						index = int(j*(WIDTH+1)+path-POURER+(WIDTH/2))
						DRAW = DRAW[:index-1] + "#" + DRAW[index:]
				else:
					print("yolo")
			previous_i, previous_j = i, j

	DRAW = DRAW[:(WIDTH+1)*(max_row+2)] + "".join(["#" for i in range(WIDTH)]) + DRAW[(WIDTH+1)*(max_row+3)-1:]
	print(DRAW)
	print(count_sand(DRAW))


