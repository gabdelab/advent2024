file = '/Users/gabrieldelaboulaye/Downloads/data.txt'

if __name__ == "__main__":
	m1 = 0
	m2 = 0
	m3 = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
		for i in data.split("\n\n"):
			try:
				total = sum([int(j) for j in i.split("\n")])
			except:
				pass
			if total >= m1:
				m3 = m2
				m2 = m1
				m1 = total
			elif total >= m2:
				m3 = m2
				m2 = total
			elif total >= m3:
				m3 = total
	print(m1)
	print(m2)
	print(m3)
	print(m1+m2+m3)