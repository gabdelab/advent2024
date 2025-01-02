import re

# file = 'data/15_ex.txt'
# ROW = 10


file = 'data/15.txt'
ROW = 2000000

START = -2000000
STOP = 6000000

# Algo:
# You can be a beacon if the distance to all sensors is larger
# than their distance to their closest beacon

# A beacon can not exist if it is closer from one sensor that its closest beacon


class Sensor():
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Sensor at (%d,%d) - beacon at (%d,%d)" % (self.x, self.y, self.x_beacon, self.y_beacon)

	def set_closest_beacon(self, x_beacon, y_beacon):
		self.x_beacon = x_beacon
		self.y_beacon = y_beacon
		self.distance = self.distance_to_closest_beacon()

	def distance_to_closest_beacon(self):
		return abs(self.x - self.x_beacon) + abs(self.y - self.y_beacon)

	def distance_to_beacon(self, x_beacon, y_beacon):
		return abs(self.x - x_beacon) + abs(self.y - y_beacon)


if __name__ == "__main__":
	sensors = []
	beacons = []
	with open(file, 'r') as open_file:
		data = open_file.read()

	for i in data.splitlines():
		sensor, beacon = i.split(":")[:2]
		sensor = sensor[10:].split(", ")
		beacon = beacon[22:].split(", ")
		my_sensor = Sensor(int(sensor[0][2:]), int(sensor[1][2:]))
		my_sensor.set_closest_beacon(int(beacon[0][2:]), int(beacon[1][2:]))
		sensors.append(my_sensor)
		beacons.append((int(beacon[0][2:]), int(beacon[1][2:])))
	print(sensors)

	total = []
	for i in range(START, STOP):
		found = False
		for s in sensors:
			# TODO if i put <= i got 27, if i put < i got 25 but i need 26
			if s.distance_to_beacon(i, ROW) <= s.distance:
				print("%s %s - %s (%s vs %s)" % (i, ROW, s, s.distance_to_beacon(i, ROW), s.distance))
				found = True
				break
			if s.x_beacon == i and s.y_beacon == ROW:
				found = True
				break
		if found and (i, ROW) not in beacons:
			total.append(i)
			continue

	print(len(total))
	# print(total)