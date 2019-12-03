def getwire(line):
	x, y, s = 0, 0, 0
	wire = [(x, y, s)]
	for e in line:
		dirx = 1 if e[0] == "R" else -1 if e[0] == "L" else 0
		diry = 1 if e[0] == "U" else -1 if e[0] == "D" else 0
		x += dirx * int(e[1:])
		y += diry * int(e[1:])
		s += int(e[1:])
		wire.append((x, y, s))
	return wire

with open("Input.txt", "r") as f:
	wire1 = getwire(f.readline().split(","))
	wire2 = getwire(f.readline().split(","))

intersections = []
for i in range(len(wire1)-1):
	for j in range(len(wire2)-1):
		if wire1[i][0] == wire1[i+1][0] and wire2[j][1] == wire2[j+1][1] and ((wire1[i][1] > wire2[j][1] and wire1[i+1][1] < wire2[j][1]) or (wire1[i][1] < wire2[j][1] and wire1[i+1][1] > wire2[j][1])) and ((wire2[j][0] > wire1[i][0] and wire2[j+1][0] < wire1[i][0]) or (wire2[j][0] < wire1[i][0] and wire2[j+1][0] > wire1[i][0])):
			intersections.append((wire1[i][2] + wire2[j][2] + abs(wire1[i][1] - wire2[j][1]) + abs(wire2[j][0] - wire1[i][0]), wire1[i][0], wire2[j][1]))
		elif wire1[i][1] == wire1[i+1][1] and wire2[j][0] == wire2[j+1][0] and ((wire1[i][0] > wire2[j][0] and wire1[i+1][0] < wire2[j][0]) or (wire1[i][0] < wire2[j][0] and wire1[i+1][0] > wire2[j][0])) and ((wire2[j][1] > wire1[i][1] and wire2[j+1][1] < wire1[i][1]) or (wire2[j][1] < wire1[i][1] and wire2[j+1][1] > wire1[i][1])):
			intersections.append((wire2[j][2] + wire1[i][2] + abs(wire2[j][1] - wire1[i][1]) + abs(wire1[i][0] - wire2[j][0]), wire2[j][0], wire1[i][1]))
intersections.sort()

print(intersections[0][0])