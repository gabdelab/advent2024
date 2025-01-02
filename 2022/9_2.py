file = 'data/9.txt'

# We will consider that first dimension is horizontal
# and going down means increasing indexes

def get_head_position(head_position, direction):
	if direction == "D":
		return (head_position[0], head_position[1]+1)
	if direction == "U":
		return (head_position[0], head_position[1]-1)
	if direction == "R":
		return (head_position[0]+1, head_position[1])
	if direction == "L":
		return (head_position[0]-1, head_position[1])


def get_tail_position(head_position, new_head_position, previous_tail_position, direction):
	x_head, y_head = head_position
	x_new_head, y_new_head = new_head_position
	x_tail, y_tail = previous_tail_position
	new_direction = direction

	if direction == "":
		# print("a")
		return previous_tail_position, ""

	# Case 0: head doesn't move, tail doesn't either
	if head_position == new_head_position:
		# print("b")
		return previous_tail_position, ""

	# Case 1: head covers tail before or after the move: tail doesn't move
	if head_position == previous_tail_position or new_head_position == previous_tail_position:
		# print("c")
		return previous_tail_position, ""

	# Case 2: head and tail were on same row/column, distance increases
	if x_tail == x_head and y_tail > y_head and direction == "U":
		# print("d")
		return head_position, "U"
	if x_tail == x_head and y_tail < y_head and direction == "D":
		# print("e")
		return head_position, "D"
	if y_tail == y_head and x_tail > x_head and direction == "L":
		# print("f")
		return head_position, "L"
	if y_tail == y_head and x_tail < x_head and direction == "R":
		# print("g")
		return head_position, "R"

	# Case 3: head and tail were in diagonal, distance increases
	# In each of these cases, head_position is returned
	if x_tail < x_head and y_tail < y_head and direction == "R":
		# print("h")
		return head_position, "diagonal"
	if x_tail < x_head and y_tail < y_head and direction == "D":
		# print("i")
		return head_position, "diagonal"
	if x_tail > x_head and y_tail < y_head and direction == "L":
		# print("j")
		return head_position, "diagonal"
	if x_tail > x_head and y_tail < y_head and direction == "D":
		# print("k")
		return head_position, "diagonal"
	if x_tail < x_head and y_tail > y_head and direction == "R":
		# print("l")
		return head_position, "diagonal"
	if x_tail < x_head and y_tail > y_head and direction == "U":
		# print("m")
		return head_position, "diagonal"
	if x_tail > x_head and y_tail > y_head and direction == "L":
		# print("n")
		return head_position, "diagonal"
	if x_tail > x_head and y_tail > y_head and direction == "U":
		# print("o")
		return head_position, "diagonal"

	# New case: 
	# Head moves on diagonal. In this case tail always moves in diagonal as well in the same direction as head
	if x_new_head != x_head and y_new_head != y_head:
		# Case 0: head and tail are neighbors. tail doesn't move
		# First case: head now shares x or y with tail. in this case, tails get closer
		if x_new_head == x_tail:
			if abs(y_new_head - y_tail) == 1:
				return previous_tail_position, ""
			if y_new_head > y_head:
				return (x_tail, y_tail+1), "D"
			return (x_tail, y_tail-1), "U"
		if y_new_head == y_tail:
			if abs(x_new_head - x_tail) == 1:
				return previous_tail_position, ""
			if x_new_head > x_head:
				return (x_tail +1, y_tail), "R"
			return (x_tail-1, y_tail), "L"
		# In this case tail always moves in diagonal as well in the same direction as head
		return (x_tail + x_new_head - x_head, y_tail + y_new_head - y_head), "diagonal"

	# print("q")
	# Case 4: head and tail were in diagonal, head gets closer -> tail doesn't move
	# Case 5: head and tail were on same row/column, head moves to diagonal -> no move
	return previous_tail_position, ""

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()

	# Start at the grid center to be sure not to have any issues
	position = (15, 15)
	head_position = position
	tail_1_position = position
	tail_2_position = position
	tail_3_position = position
	tail_4_position = position
	tail_5_position = position
	tail_6_position = position
	tail_7_position = position
	tail_8_position = position
	tail_9_position = position

	covered_positions = {position for i in range(1)}

	positions = """............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
............................
"""
	yolo = positions
	for head_moves in data.split("\n"):
		if head_moves == "":
			break
		first_direction, count = head_moves.split(" ")[:2]
		for i in range(int(count)):
			mycopy = yolo
			new_head_position = get_head_position(head_position, first_direction)
			new_tail_1_position, direction = get_tail_position(head_position, new_head_position, tail_1_position, first_direction)
			new_tail_2_position, direction = get_tail_position(tail_1_position, new_tail_1_position, tail_2_position, direction)
			new_tail_3_position, direction = get_tail_position(tail_2_position, new_tail_2_position, tail_3_position, direction)
			new_tail_4_position, direction = get_tail_position(tail_3_position, new_tail_3_position, tail_4_position, direction)
			new_tail_5_position, direction = get_tail_position(tail_4_position, new_tail_4_position, tail_5_position, direction)
			new_tail_6_position, direction = get_tail_position(tail_5_position, new_tail_5_position, tail_6_position, direction)
			new_tail_7_position, direction = get_tail_position(tail_6_position, new_tail_6_position, tail_7_position, direction)
			new_tail_8_position, direction = get_tail_position(tail_7_position, new_tail_7_position, tail_8_position, direction)
			new_tail_9_position, direction = get_tail_position(tail_8_position, new_tail_8_position, tail_9_position, direction)

			tail_1_position = new_tail_1_position
			tail_2_position = new_tail_2_position
			tail_3_position = new_tail_3_position
			tail_4_position = new_tail_4_position
			tail_5_position = new_tail_5_position
			tail_6_position = new_tail_6_position
			tail_7_position = new_tail_7_position
			tail_8_position = new_tail_8_position
			if tail_9_position != new_tail_9_position:
				print(new_tail_9_position)
			tail_9_position = new_tail_9_position
			head_position = new_head_position

			covered_positions = covered_positions.union(tail_9_position for i in range(1))
			a0, b0 = head_position
			a1, b1 = tail_1_position
			a2, b2 = tail_2_position
			a3, b3 = tail_3_position
			a4, b4 = tail_4_position
			a5, b5 = tail_5_position
			a6, b6 = tail_6_position
			a7, b7 = tail_7_position
			a8, b8 = tail_8_position
			a9, b9 = tail_9_position

			index0 = a0 + b0*29
			index1 = a1 + b1*29
			index2 = a2 + b2*29
			index3 = a3 + b3*29
			index4 = a4 + b4*29
			index5 = a5 + b5*29
			index6 = a6 + b6*29
			index7 = a7 + b7*29
			index8 = a8 + b8*29
			index9 = a9 + b9*29

			positions = positions[:index9-1] + "9" + positions[index9:]
			mycopy = mycopy[:index0-1] + "H" + mycopy[index0:]
			mycopy = mycopy[:index1-1] + "1" + mycopy[index1:]
			mycopy = mycopy[:index2-1] + "2" + mycopy[index2:]
			mycopy = mycopy[:index3-1] + "3" + mycopy[index3:]
			mycopy = mycopy[:index4-1] + "4" + mycopy[index4:]
			mycopy = mycopy[:index5-1] + "5" + mycopy[index5:]
			mycopy = mycopy[:index6-1] + "6" + mycopy[index6:]
			mycopy = mycopy[:index7-1] + "7" + mycopy[index7:]
			mycopy = mycopy[:index8-1] + "8" + mycopy[index8:]
			mycopy = mycopy[:index9-1] + "9" + mycopy[index9:]
	print(positions)
	print(covered_positions)
	print(len(covered_positions))