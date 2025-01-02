from itertools import permutations

file = 'data/12.txt'
WIDTH = 143
HEIGHT = 41
START = (20, 0)

# file = 'data/12_ex.txt'
# WIDTH = 8
# HEIGHT = 5
# START = (0, 0)


POINTS = {
	"S": 1,
	"a": 1,
	"b": 2,
	"c": 3,
	"d": 4,
	"e": 5,
	"f": 6,
	"g": 7,
	"h": 8,
	"i": 9,
	"j": 10,
	"k": 11,
	"l": 12,
	"m": 13,
	"n": 14,
	"o": 15,
	"p": 16,
	"q": 17,
	"r": 18,
	"s": 19,
	"t": 20,
	"u": 21,
	"v": 22,
	"w": 23,
	"x": 24,
	"y": 25,
	"z": 26,
	"E": 26
}

dataPoints = {}
bestPath= {}

class Point:

	def __init__(self, x, y, value=None, letter=None):
		self.row = y 
		self.column = x
		self.height = None
		if value is not None and self.height is None:
			self.height = value
			self.letter = letter

	def __repr__(self):
		return "(%d, %d)-%s" % (self.row, self.column, self.letter)

	def visitable_neighbors(self):
		neighbors = {
			"up": dataPoints.get(self.row-1, {}).get(self.column, None), 
			"down": dataPoints.get(self.row+1, {}).get(self.column, None),
			"right": dataPoints.get(self.row, {}).get(self.column+1, None),
			"left": dataPoints.get(self.row, {}).get(self.column-1, None)
		}
		# first get the list
		if self.row == HEIGHT - 1:
			neighbors.pop("down")
		if self.column == WIDTH - 1:
			neighbors.pop("right")
		if self.column == 0:
			neighbors.pop("left")
		if self.row == 0:
			neighbors.pop("up")

		to_pop = []
		for direction, point in neighbors.items():
			if point.height > self.height + 1:
				to_pop.append(direction)
		for i in to_pop:
			neighbors.pop(i)
		self.neighbors = neighbors
		# print(["%s - %s %s" % (self, i,j) for i, j in self.neighbors.items()])

	def reverse_neighbors(self):
		"""All points that can visit me"""
		self.reverse_neighbors = []
		for j in range(WIDTH):
			for i in range(HEIGHT):
				if self in dataPoints[i][j].neighbors.values():
					self.reverse_neighbors.append(dataPoints[i][j])

def get_paths(current_point, previous_path, max_length):
	"""
		returns the shortest path to go from current_point to E
	"""
	if current_point.letter == "E":
		previous_path.append(current_point)
		bestPath[current_point.row][current_point.column] = [current_point]
		# print(previous_path)
		return previous_path
	if max_length == 0:
		return []
	solutions = []
	for direction, point in current_point.neighbors.items():
		if point in previous_path:
			# print("previous_path: %s, current_point: %s, point: %s" % (previous_path, current_point, point))
			continue
		if bestPath[point.row][point.column] is not None:
			best = bestPath[point.row][point.column]
			# best.insert(0, current_point)
			solutions.append(best.copy())
			continue
		do_copy = previous_path.copy()
		do_copy.append(current_point)
		obtained_path = get_paths(point, do_copy, max_length - 1)
		# print("%s - %s (%s) XXXXXXXXXXXX %s " % (current_point, direction, previous_path, obtained_path))

		# if bestPath[point.row][point.column] is None:
		# 	bestPath[point.row][point.column] = obtained_path
		if len(obtained_path) >=1 and obtained_path[-1].letter=="E":
			solutions.append(obtained_path)
	min_path = 10000
	min_solution= []
	# print(solutions)
	for j in solutions:
		if len(j) < min_path:
			min_path = len(j)
			min_solution = j
	if bestPath[current_point.row][current_point.column] is None:
		didier = min_solution.copy()

		bestPath[current_point.row][current_point.column] = didier
	return min_solution


def yolo():
	done = set()
	for _, i in dataPoints.items():
		for _, j in i.items():
			if j.letter == "E":
				done.add(j)
				bestPath[j.row][j.column] = [j]
	while bestPath[START[0]][START[1]] is None:
		for index, neighbor in enumerate(done):
			to_add = set()
			for point in neighbor.reverse_neighbors:
				didier = bestPath[neighbor.row][neighbor.column].copy()
				didier.insert(0, point)
				if bestPath[point.row][point.column] is not None:
					if len(bestPath[point.row][point.column]) < len(didier):
						continue
				bestPath[point.row][point.column] = didier
				to_add.add(point)
			done = done.union(to_add)

if __name__ == "__main__":
	grid = []
	with open(file, 'r') as open_file:
		data = open_file.read()

	for index_row, row in enumerate(data.split("\n")):
		dataPoints[index_row] = {}
		bestPath[index_row] = {}
		for index, letter in enumerate(row):
			grid.append(POINTS[letter])
			bestPath[index_row][index] = []
			dataPoints[index_row][index] = Point(index, index_row, grid[index_row*WIDTH + index], letter)

	for row in range(HEIGHT):
		for column in range(WIDTH):
			bestPath[row][column] = None
			dataPoints[row][column].visitable_neighbors()
	for row in range(HEIGHT):
		for column in range(WIDTH):
			dataPoints[row][column].reverse_neighbors()


	start_point = dataPoints[START[0]][START[1]]
	yolo()
	for row in range(HEIGHT):
		for column in range(WIDTH):
			if dataPoints[row][column].letter in ('a', 'S'):
				if bestPath[row][column]:
					print(row, column, len(bestPath[row][column]) - 1)

	# print(len(bestPath[START[0]][START[1]])-1)
	# results = get_paths(start_point, [], WIDTH * HEIGHT)
	# # print(start_point)
	# # print(len([str(i) for i in results]))
	# # print([str(i) for i in results])
	# print(bestPath)
