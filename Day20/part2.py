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
			inner = x >= 3 and x <= len(maze[y])-3 and y >= 3 and y <= len(maze)-3
			if maze[y-1][x] == ".":
				portals.append([maze[y][x] + maze[y+1][x], x, y-1, inner])
			elif maze[y+1][x] == ".":
				portals.append([maze[y-1][x] + maze[y][x], x, y+1, inner])
			elif maze[y][x-1] == ".":
				portals.append([maze[y][x] + maze[y][x+1], x-1, y, inner])
			elif maze[y][x+1] == ".":
				portals.append([maze[y][x-1] + maze[y][x], x+1, y, inner])

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
				teleportsto.append([portals[j][1], portals[j][2], portals[i][3]])
				teleportsto.append([portals[i][1], portals[i][2], portals[j][3]])

stack = [[copy.copy(i) for i in maze]]
stack[0][start[1]][start[0]] = "@"

steps = 0
while stack[0][end[1]][end[0]] == ".":
	tmpstack = [[copy.copy(j) for j in i] for i in stack]
	for i in range(len(stack)):
		for y in range(1, len(stack[i])-1):
			for x in range(1, len(stack[i][y])-1):
				if stack[i][y][x] == "@":
					if stack[i][y-1][x] == ".":
						tmpstack[i][y-1][x] = "@"
					if stack[i][y+1][x] == ".":
						tmpstack[i][y+1][x] = "@"
					if stack[i][y][x-1] == ".":
						tmpstack[i][y][x-1] = "@"
					if stack[i][y][x+1] == ".":
						tmpstack[i][y][x+1] = "@"
					if [x,y] in teleportsfrom:
						pos = teleportsto[teleportsfrom.index([x,y])]
						if pos[2]:
							if i+1 == len(tmpstack):
								tmpstack.append([copy.copy(i) for i in maze])
							tmpstack[i+1][pos[1]][pos[0]] = "@"
						else:
							if i > 0:
								tmpstack[i-1][pos[1]][pos[0]] = "@"
	stack = tmpstack
	steps += 1

print(steps)