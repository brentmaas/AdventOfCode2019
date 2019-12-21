import copy

maze = []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		maze.append([i for i in line.replace("\n", "")])
		line = f.readline()

portals = []

for y in range(1, len(maze)-1):
	for x in range(1, len(maze[y])-1):
		if ord(maze[y][x]) >= ord("A") and ord(maze[y][x]) <= ord("Z"):
			if maze[y-1][x] == ".":
				portals.append([maze[y][x] + maze[y+1][x], x, y-1])
			elif maze[y+1][x] == ".":
				portals.append([maze[y-1][x] + maze[y][x], x, y+1])
			elif maze[y][x-1] == ".":
				portals.append([maze[y][x] + maze[y][x+1], x-1, y])
			elif maze[y][x+1] == ".":
				portals.append([maze[y][x-1] + maze[y][x], x+1, y])

teleportsfrom = []
teleportsto = []

for i in range(len(portals)):
	if portals[i][0] == "AA":
		start = [portals[i][1], portals[i][2]]
	elif portals[i][0] == "ZZ":
		end = [portals[i][1], portals[i][2]]
	elif not [portals[i][1], portals[i][2]] in teleportsfrom:
		for j in range(i+1, len(portals)):
			if portals[i][0] == portals[j][0]:
				teleportsfrom.append([portals[i][1], portals[i][2]])
				teleportsfrom.append([portals[j][1], portals[j][2]])
				teleportsto.append([portals[j][1], portals[j][2]])
				teleportsto.append([portals[i][1], portals[i][2]])

maze[start[1]][start[0]] = "@"

steps = 0
while maze[end[1]][end[0]] == ".":
	tmpmaze = [copy.copy(i) for i in maze]
	for y in range(1, len(maze)-1):
		for x in range(1, len(maze[y])-1):
			if maze[y][x] == "@":
				if maze[y-1][x] == ".":
					tmpmaze[y-1][x] = "@"
				if maze[y+1][x] == ".":
					tmpmaze[y+1][x] = "@"
				if maze[y][x-1] == ".":
					tmpmaze[y][x-1] = "@"
				if maze[y][x+1] == ".":
					tmpmaze[y][x+1] = "@"
				if [x,y] in teleportsfrom:
					pos = teleportsto[teleportsfrom.index([x,y])]
					tmpmaze[pos[1]][pos[0]] = "@"
	maze = tmpmaze
	steps += 1

print(steps)