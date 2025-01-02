import re
import itertools


# file = 'data/15_ex.txt'
# MAX = 20

file = 'data/15.txt'
MAX = 4000000

# Algo:
# You can be a beacon if the distance to all sensors is larger
# than their distance to their closest beacon

# A beacon can not exist if it is closer from one sensor that its closest beacon


class Sensor():
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Sensor at (%d,%d) - rayon %d" % (self.x, self.y, self.distance)

	def set_closest_beacon(self, x_beacon, y_beacon):
		self.x_beacon = x_beacon
		self.y_beacon = y_beacon
		self.distance = self.distance_to_closest_beacon()
		# self.outer_border = self.outer_border()

	def distance_to_closest_beacon(self):
		return abs(self.x - self.x_beacon) + abs(self.y - self.y_beacon)

	def distance_to_beacon(self, x_beacon, y_beacon):
		return abs(self.x - x_beacon) + abs(self.y - y_beacon)

	def outer_border(self):
		return set([(self.x + self.distance+k, self.y + self.distance+k) for k in range(self.distance)]+
			[(self.x + self.distance+k, self.y - self.distance+k) for k in range(self.distance)]+
			[(self.x - self.distance+k, self.y + self.distance+k) for k in range(self.distance)]+
			[(self.x - self.distance+k, self.y - self.distance+k) for k in range(self.distance)])

if __name__ == "__main__":
	sensors = []
	beacons = []
	with open(file, 'r') as open_file:
		data = open_file.read()

	for i in data.splitlines():
		print(i)
		sensor, beacon = i.split(":")[:2]
		sensor = sensor[10:].split(", ")
		beacon = beacon[22:].split(", ")
		my_sensor = Sensor(int(sensor[0][2:]), int(sensor[1][2:]))
		my_sensor.set_closest_beacon(int(beacon[0][2:]), int(beacon[1][2:]))
		sensors.append(my_sensor)
		beacons.append((int(beacon[0][2:]), int(beacon[1][2:])))
	print(sensors)

	covered_area = {}
	total = []
	for column in range(3256000, 3258000):
		if column % 10 == 0:
			print(column)
		difference = 0
		for row in range(2572000, 2574000):
			found = False
			if difference > 0:
				difference -= 1
				found = True
				continue
			# Compute all distances to beacon, take the shortest one
			difference = max([s.distance - s.distance_to_beacon(column, row) for s in sensors])
			# Difference is negative: the current point is further from all beacons than their vision distance
			if difference < 0:
				total.append((column, row))
				break
		if len(total)==1:
			break
	# total = []
	# for i in itertools.permutations(sensors):
	# 	s1, s2, s3, s4 = i[:4]
	# 	yolo = s1.outer_border.intersection(s2.outer_border).intersection(s3.outer_border).intersection(s4.outer_border)
	# 	if len(yolo) > 0:
	# 		total.append(yolo)
	# 	if len(total) > 0:
	# 		break
	print(len(total))
	print(total)
	print((total[0][0]*4000000)+total[0][1])