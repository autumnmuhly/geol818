print('hello world')
with open('../data/All.deep_sorted','r') as file:
    headerline = infile.readline()
    for line in file:
        items = line.split()
	mag = float(items[3])
	if mag > 6 and mag < 8:
		print(items[1])
