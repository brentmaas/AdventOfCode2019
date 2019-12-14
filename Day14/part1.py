import numpy as np

reactions = {}
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		l = line.replace("\n", "").replace(" => ", ", ").split(", ")
		reactions[l[-1].split(" ")[1]] = [int(l[-1].split(" ")[0]), [[int(el.split(" ")[0]), el.split(" ")[1]] for el in l[:-1]]]
		line = f.readline()

ore = 0
todo = reactions["FUEL"][1]
leftover = {}
for i in reactions:
	leftover[i] = 0
while len(todo) > 0:
	recipe = reactions[todo[0][1]]
	if leftover[todo[0][1]] < todo[0][0]:
		n = int(np.ceil((todo[0][0] - leftover[todo[0][1]]) / recipe[0]))
		for req in recipe[1]:
			if req[1] == "ORE":
				ore += req[0] * n
			else:
				todo.append([req[0] * n, req[1]])
		leftover[todo[0][1]] += n * recipe[0] - todo[0][0]
	else:
		leftover[todo[0][1]] -= todo[0][0]
	todo = todo[1:]

print(ore)