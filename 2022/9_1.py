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

	# Case 1: head covers tail before or after the move: tail doesn't move
	if head_position == previous_tail_position or new_head_position == previous_tail_position:
		return previous_tail_position

	# Case 2: head and tail were on same row/column, distance increases
	if x_tail == x_head and y_tail > y_head and direction == "U":
		return head_position
	if x_tail == x_head and y_tail < y_head and direction == "D":
		return head_position
	if y_tail == y_head and x_tail > x_head and direction == "L":
		return head_position
	if y_tail == y_head and x_tail < x_head and direction == "R":
		return head_position

	# Case 3: head and tail were in diagonal, distance increases
	# In each of these cases, head_position is returned
	if x_tail < x_head and y_tail < y_head and direction == "R":
		return head_position
	if x_tail < x_head and y_tail < y_head and direction == "D":
		return head_position
	if x_tail > x_head and y_tail < y_head and direction == "L":
		return head_position
	if x_tail > x_head and y_tail < y_head and direction == "D":
		return head_position
	if x_tail < x_head and y_tail > y_head and direction == "R":
		return head_position
	if x_tail < x_head and y_tail > y_head and direction == "U":
		return head_position
	if x_tail > x_head and y_tail > y_head and direction == "L":
		return head_position
	if x_tail > x_head and y_tail > y_head and direction == "U":
		return head_position

	# Case 4: head and tail were in diagonal, head gets closer -> tail doesn't move
	# Case 5: head and tail were on same row/column, head moves to diagonal -> no move
	return previous_tail_position

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()

	# Start at the grid center to be sure not to have any issues
	position = (1000, 1000)
	head_position = position
	covered_positions = {position for i in range(1)}

	for head_moves in data.split("\n"):
		if head_moves == "":
			break
		direction, count = head_moves.split(" ")[:2]
		for i in range(int(count)):
			new_head_position = get_head_position(head_position, direction)
			tail_position = get_tail_position(head_position, new_head_position, position, direction)
			position = tail_position
			head_position = new_head_position
			print(tail_position)
			covered_positions = covered_positions.union(tail_position for i in range(1))

	print(len(covered_positions))