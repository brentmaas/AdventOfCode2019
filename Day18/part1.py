import copy

maze = []
with open("Test3.txt", "r") as f:
	line = f.readline()
	while line:
		maze.append([i for i in line.replace("\n", "")])
		line = f.readline()

stepfield = [[0] * len(l) for l in maze]
dofilter = True
while dofilter:
	#tmpmaze = [copy.copy(l) for l in maze]
	dofilter = False
	for y in range(1, len(maze)-1):
		for x in range(1, len(maze[0])-1):
			if maze[y][x] == "." or (ord(maze[y][x]) >= ord("A") and ord(maze[y][x]) <= ord("Z")):
				walls = 0
				walls += 1 if maze[y-1][x] == "#" else 0
				walls += 1 if maze[y+1][x] == "#" else 0
				walls += 1 if maze[y][x-1] == "#" else 0
				walls += 1 if maze[y][x+1] == "#" else 0
				paths = 0
				paths += 1 if maze[y-1][x] == "." else 0
				paths += 1 if maze[y+1][x] == "." else 0
				paths += 1 if maze[y][x-1] == "." else 0
				paths += 1 if maze[y][x+1] == "." else 0
				if walls >= 3:
					maze[y][x] = "#"
					dofilter = True
					break
				elif ord(maze[y][x]) >= ord("A") and ord(maze[y][x]) <= ord("Z") and walls == 2 and paths == 1:
					if maze[y-1][x] == ".":
						nx, ny = x, y-1
					elif maze[y+1][x] == ".":
						nx, ny = x, y+1
					elif maze[y][x-1] == ".":
						nx, ny = x-1, y
					elif maze[y][x+1] == ".":
						nx, ny = x+1, y
					maze[ny][nx] = maze[y][x]
					maze[y][x] = "."
					dofilter = True
					break
			elif ord(maze[y][x]) >= ord("a") and ord(maze[y][x]) <= ord("z") and (maze[y-1][x] == "." or maze[y+1][x] == "." or maze[y][x-1] == "." or maze[y][x+1] == "."):
				walls = 0
				walls += 1 if maze[y-1][x] == "#" else 0
				walls += 1 if maze[y+1][x] == "#" else 0
				walls += 1 if maze[y][x-1] == "#" else 0
				walls += 1 if maze[y][x+1] == "#" else 0
				if walls >= 3:
					if not (maze[y-1][x] == "#"):
						nx, ny = x, y-1
					elif not (maze[y+1][x] == "#"):
						nx, ny = x, y+1
					elif not (maze[y][x-1] == "#"):
						nx, ny = x-1, y
					elif not (maze[y][x+1] == "#"):
						nx, ny = x+1, y
					maze[ny][nx] = maze[y][x]
					stepfield[ny][nx] = stepfield[y][x] + 1
					maze[y][x] = "#"
					stepfield[y][x] = 0
					dofilter = True
					break
		if dofilter:
			break
	#maze = tmpmaze

for l in maze:
	print("".join(l))

def floodfillfind(maze, keys):
	ffmaze = copy.copy(maze)
	pos, step = [], []
	found = True
	i = 0
	while found:
		tmpffmaze = [copy.copy(l) for l in ffmaze]
		found = False
		i += 1
		for y in range(1, len(ffmaze) - 1):
			for x in range(1, len(ffmaze[0]) - 1):
				if (ffmaze[y][x] == "." or chr(ord(ffmaze[y][x]) - ord("A") + ord("a")) in keys) and (ffmaze[y-1][x] == "@" or ffmaze[y+1][x] == "@" or ffmaze[y][x-1] == "@" or ffmaze[y][x+1] == "@"):
					tmpffmaze[y][x] = "@"
					found = True
				elif ord(ffmaze[y][x]) >= ord("a") and ord(ffmaze[y][x]) <= ord("z") and (ffmaze[y-1][x] == "@" or ffmaze[y+1][x] == "@" or ffmaze[y][x-1] == "@" or ffmaze[y][x+1] == "@"):
					pos.append([x,y])
					step.append(i)
					tmpffmaze[y][x] = "@"
					found = True
		ffmaze = tmpffmaze
	return pos, step

stop = False
for y in range(0, len(maze)):
	for x in range(0, len(maze[0])):
		if maze[y][x] == "@":
			stop = True
			break
	if stop:
		break

instances = [[maze, [], [x,y], 0]]
finished = []

while len(instances) > 0:
	print(f"{len(instances)}, {len(instances[0][1])}        ", end="\r")
	pos, step = floodfillfind(instances[0][0], instances[0][1])
	for i in range(len(pos)):
		step[i] += stepfield[pos[i][1]][pos[i][0]] + stepfield[instances[0][2][1]][instances[0][2][0]]
	if len(pos) == 0:
		finished.append(instances[0])
	else:
		for i in range(len(pos)):
			newkeys = instances[0][1] + [instances[0][0][pos[i][1]][pos[i][0]]]
			newmaze = [copy.copy(l) for l in instances[0][0]]
			newmaze[instances[0][2][1]][instances[0][2][0]] = "."
			newmaze[pos[i][1]][pos[i][0]] = "@"
			append = True
			for j in range(1, len(instances)):
				if instances[j][3] < instances[0][3] + step[i] and instances[j][2][0] == pos[i][0] and instances[j][2][1] == pos[i][1]:
					good = True
					sameset = True
					for k in range(len(instances[j][1])):
						if not (instances[j][1][k] in newkeys):
							good = False
							sameset = False
							break
					for k in range(len(newkeys)):
						if not (newkeys[k] in instances[j][1]):
							good = True
							sameset = False
							break
					if not good or sameset:
						append = False
						break
			if append:
				instances.append([newmaze, newkeys, pos[i], instances[0][3] + step[i]])
	instances = instances[1:]

min = finished[0][3]
for i in range(1, len(finished)):
	if finished[i][3] < min:
		min = finished[i][3]

print(min, "         ")