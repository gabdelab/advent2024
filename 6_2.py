from collections import defaultdict

class Point:
    def __init__(self, row, col, value, visited=False):
        self.row = row
        self.col = col 
        self.value = value
        self.initial_value = value
        self.visited = visited
        self.visited_directions = set()
    
    def set_visited(self):
        self.visited = True

def reset_data(data):
    for row in data.values():
        for point in row:
            point.visited = False
            point.visited_directions = set()
            point.value = point.initial_value

data = defaultdict(list)
direction = 'up'
with open("data/6.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        data[i] = []
        for j, col in enumerate(line.strip()):
            visited = False
            if col not in ['.', '#']:
                visited = True
                current = (i, j)
            data[i].append(Point(i, j, col, visited))
initial_current = current
initial_data = data.copy()

counter = 0
solutions = []
for i in range(len(data)):
    print(i)
    for j in range(len(data)):
        reset_data(data)
        current = initial_current
        direction = 'up'
        if data[i][j].value == "#":
            continue
        data[i][j].value = "#"
        while True:
            if direction in data[current[0]][current[1]].visited_directions:
                counter += 1
                solutions.append((i, j))
                break
            data[current[0]][current[1]].visited_directions.add(direction)

            if direction == 'up':
                tmp_current = (current[0] - 1, current[1])
                if tmp_current[0] < 0 or tmp_current[0] >= len(data) or tmp_current[1] < 0 or tmp_current[1] >= len(data[tmp_current[0]]):
                    break
                if data[tmp_current[0]][tmp_current[1]].value != "#":
                    current = tmp_current
                else:
                    direction = 'right'
                    continue
            elif direction == 'down':
                tmp_current = (current[0] + 1, current[1])
                if tmp_current[0] < 0 or tmp_current[0] >= len(data) or tmp_current[1] < 0 or tmp_current[1] >= len(data[tmp_current[0]]):
                    break
                if data[tmp_current[0]][tmp_current[1]].value != "#":
                    current = tmp_current
                else:
                    direction = 'left'
                    continue
            elif direction == 'left':
                tmp_current = (current[0], current[1] - 1)
                if tmp_current[0] < 0 or tmp_current[0] >= len(data) or tmp_current[1] < 0 or tmp_current[1] >= len(data[tmp_current[0]]):
                    break
                if data[tmp_current[0]][tmp_current[1]].value != "#":
                    current = tmp_current
                else:
                    direction = 'up'
                    continue
            elif direction == 'right':
                tmp_current = (current[0], current[1] + 1)
                if tmp_current[0] < 0 or tmp_current[0] >= len(data) or tmp_current[1] < 0 or tmp_current[1] >= len(data[tmp_current[0]]):
                    break
                if data[tmp_current[0]][tmp_current[1]].value != "#":
                    current = tmp_current
                else:
                    direction = 'down'
                    continue
            data[current[0]][current[1]].set_visited()
print(counter)
