from collections import defaultdict

class Point:
    def __init__(self, row, col, value, visited=False):
        self.row = row
        self.col = col 
        self.value = value
        self.visited = visited
    
    def set_visited(self):
        self.visited = True

data = defaultdict(list)
direction = 'up'
with open("data/6_ex.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        data[i] = []
        for j, col in enumerate(line.strip()):
            visited = False
            if col not in ['.', '#']:
                visited = True
                current = (i, j)
            data[i].append(Point(i, j, col, visited))

while True:
    print(current, direction)
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

print(sum(1 for row in data.values() for point in row if point.visited))

