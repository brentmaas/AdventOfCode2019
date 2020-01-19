import copy

maze = []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		maze.append([i for i in line.replace("\n", "")])
		line = f.readline()

keys = []
for i in maze:
	for j in i:
		if ord(j) >= ord("a") and ord(j) <= ord("z"):
			keys.append(j)

def floodfillfind(maze, start):
	visited = [[False for j in i] for i in maze]
	steps = []
	keys = []
	needed = []
	pos = []
	step = []
	doors = []
	for y in range(len(maze)):
		for x in range(len(maze[y])):
			if maze[y][x] == start:
				pos.append([x, y])
				step.append(0)
				doors.append([])
				break
		if len(pos) > 0:
			break
	while len(pos) > 0:
		if ord(maze[pos[0][1]][pos[0][0]]) >= ord("a") and ord(maze[pos[0][1]][pos[0][0]]) <= ord("z") and not maze[pos[0][1]][pos[0][0]] == start:
			steps.append(step[0])
			needed.append(doors[0])
			keys.append(maze[pos[0][1]][pos[0][0]])
		for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
			if maze[pos[0][1]+dy][pos[0][0]+dx] == "#" or visited[pos[0][1]+dy][pos[0][0]+dx]:
				continue
			pos.append([pos[0][0]+dx, pos[0][1]+dy])
			step.append(step[0] + 1)
			if ord(maze[pos[0][1]+dy][pos[0][0]+dx]) >= ord("A") and ord(maze[pos[0][1]+dy][pos[0][0]+dx]) <= ord("Z"):
				doors[0].append(chr(ord(maze[pos[0][1]+dy][pos[0][0]+dx]) - ord("A") + ord("a")))
			doors.append(copy.copy(doors[0]))
		visited[pos[0][1]][pos[0][0]] = True
		pos = pos[1:]
		step = step[1:]
		doors = doors[1:]
	return keys, steps, needed

paths = {}
path = {}
k, s, n = floodfillfind(maze, "@")
for i in range(len(k)):
	path[k[i]] = [s[i], n[i]]
paths["@"] = path
for i in keys:
	path = {}
	k, s, n = floodfillfind(maze, i)
	for j in range(len(k)):
		path[k[j]] = [s[j], n[j]]
	paths[i] = path

branches = [["@", [], 0]]
finished = []

while len(branches) > 0:
	print(f"{len(branches)}, {len(branches[0][1])}        ", end="\r")
	if len(branches[0][1]) == len(keys):
		finished.append(branches[0])
	else:
		append = True
		for i in range(1, len(branches)):
			if branches[i][2] < branches[0][2] and branches[i][0] == branches[0][0]:
				good = True
				sameset = True
				for j in range(len(branches[i][1])):
					if not branches[i][1][j] in branches[0][1]:
						good = False
						sameset = False
						break
				for j in range(len(branches[0][1])):
					if not branches[0][1][j] in branches[i][1]:
						good = True
						sameset = False
						break
				if not good or sameset:
					append = False
					break
		if append:
			for p in paths[branches[0][0]]:
				if not p in branches[0][1]:
					skip = False
					for p2 in paths[branches[0][0]][p][1]:
						if not p2 in branches[0][1]:
							skip = True
							break
					if not skip:
						newkeys = branches[0][1] + [p]
						"""append = True
						for i in range(1, len(branches)):
							if branches[i][2] < branches[0][2] + paths[branches[0][0]][p][0] and branches[i][0] == p:
								good = True
								sameset = True
								for j in range(len(branches[i][1])):
									if not branches[i][1][j] in newkeys:
										good = False
										sameset = False
										break
								for j in range(len(newkeys)):
									if not newkeys[j] in branches[i][1]:
										good = True
										sameset = False
										break
								if not good or sameset:
									append = False
									break
						if append:"""
						branches.append([p, newkeys, branches[0][2] + paths[branches[0][0]][p][0]])
	branches = branches[1:]

m = finished[0][2]
for i in range(1, len(finished)):
	m = min(m, finished[i][2])

print(m, "                            ")