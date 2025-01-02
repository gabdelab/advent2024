file = 'data/7.txt'

THRESHOLD = 100000
TO_DELETE = 528671

def nested_set_file(dic, keys, file, size):
	if not keys:
		dic[file] = int(size)
		return
	for key in keys[:-1]:
		dic = dic.setdefault(key, {})
	dic[keys[-1]][file] = int(size)


def nested_set_dir(dic, keys, mydir):
	if not keys:
		dic[mydir] = {}
		return
	for key in keys[:-1]:
		dic = dic.setdefault(key, {})
	dic[keys[-1]][mydir] = {}

def sum_values(my_dict):
	subdicts = [v for k, v in my_dict.items() if isinstance(v, dict)]
	ints = [v for k, v in my_dict.items() if isinstance(v, int)]
	total = sum(ints) + sum([sum_values(i) for i in subdicts])
	# if total <= THRESHOLD:
		# print(total)
	if total >= TO_DELETE and total <= 1.05*TO_DELETE:
		print(total)
	return total

if __name__ == "__main__":
	with open(file, 'r') as open_file:
		data = open_file.read()

	filedir = {}
	localdir = []
	for i in data.split("\n"):
		if i == "":
			break
		if i[0] == "$":
			if i[2:4] == "ls":
				continue
			if i[2:4] == "cd":
				if i[5:] == "..":
					localdir = localdir[:-1]
					continue
				if i[5:] == "/":
					localdir = []
				else:
					localdir.append(i[5:])
				continue
		if i[:3] == "dir":
			dir_name = i[4:]
			nested_set_dir(filedir, localdir, dir_name)
			continue	
		else:
			# new file
			size, file_name = i.split(" ")[:2]
			nested_set_file(filedir, localdir, file_name, size)
			continue
	print(filedir)


	print(sum_values(filedir))
