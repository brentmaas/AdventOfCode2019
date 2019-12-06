orbits = {}

with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		a, b = line.replace("\n", "").split(")")
		orbits[b] = (a, None)
		line = f.readline()

orbits["COM"] = (None, 0)

total = 0
for i in orbits:
	n = 0
	sub = orbits[i]
	while sub[1] is None:
		n += 1
		sub = orbits[sub[0]]
	n += sub[1]
	total += n
	orbits[i] = (orbits[i][0], n)

print(total)