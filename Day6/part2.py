orbits = {}

with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		a, b = line.replace("\n", "").split(")")
		orbits[b] = a
		line = f.readline()

orbits["COM"] = None

def getorbittrace(inp):
	l = []
	curr = inp
	while not orbits[curr] is None:
		curr = orbits[curr]
		l.append(curr)
	return l

youlist = getorbittrace("YOU")
sanlist = getorbittrace("SAN")

def getfirstcommon(l1, l2):
	i = 0
	while not l1[i] in l2:
		i += 1
	return i

youi = getfirstcommon(youlist, sanlist)
sani = getfirstcommon(sanlist, youlist)

print(youi + sani)