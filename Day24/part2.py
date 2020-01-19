import copy

state = []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		state.append([i for i in line.replace("\n", "")])
		line = f.readline()
state = [state]

def get(state, d, x, y):
	adjacent = 0
	if x == 0 and d > 0:
		adjacent += 1 if state[d-1][2][1] == "#" else 0
	if y == 0 and d > 0:
		adjacent += 1 if state[d-1][1][2] == "#" else 0
	if x == len(state[d][y])-1 and d > 0:
		adjacent += 1 if state[d-1][2][3] == "#" else 0
	if y == len(state[d])-1 and d > 0:
		adjacent += 1 if state[d-1][3][2] == "#" else 0
	if x == 1 and y == 2 and d < len(state)-1:
		for i in range(len(state[d+1])):
			adjacent += 1 if state[d+1][i][0] == "#" else 0
	if x == 3 and y == 2 and d < len(state)-1:
		for i in range(len(state[d+1])):
			adjacent += 1 if state[d+1][i][-1] == "#" else 0
	if x == 2 and y == 1 and d < len(state)-1:
		for i in range(len(state[d+1][0])):
			adjacent += 1 if state[d+1][0][i] == "#" else 0
	if x == 2 and y == 3 and d < len(state)-1:
		for i in range(len(state[d+1][-1])):
			adjacent += 1 if state[d+1][-1][i] == "#" else 0
	for dx, dy in zip([0, -1, 0, 1], [1, 0, -1, 0]):
		if x+dx >= 0 and x+dx < len(state[d][y]) and y+dy >= 0 and y+dy < len(state[d]) and not (x+dx == 2 and y+dy == 2):
			adjacent += 1 if state[d][y+dy][x+dx] == "#" else 0
	return adjacent

dd = 0
for m in range(200):
	print(m, end="\r")
	if True in [True in [state[-1][y][x] == "#" for x in range(len(state[-1][y]))] for y in range(len(state[-1]))]:
		state.append([["." for _ in range(len(state[0][0]))] for _ in range(len(state[0]))])
	if True in [True in [state[0][y][x] == "#" for x in range(len(state[0][y]))] for y in range(len(state[0]))]:
		state = [[["." for _ in range(len(state[0][0]))] for _ in range(len(state[0]))]] + state
		dd += 1
	prev = [[[copy.copy(k) for k in j] for j in i] for i in state]
	for d in range(len(state)):
		for y in range(len(state[d])):
			for x in range(len(state[d][y])):
				adjacent = get(prev, d, x, y)
				if prev[d][y][x] == "#" and not adjacent == 1:
					state[d][y][x] = "."
				elif prev[d][y][x] == "." and (adjacent == 1 or adjacent == 2):
					state[d][y][x] = "#"

bugs = 0
for d in range(len(state)):
	for y in range(len(state[d])):
		for x in range(len(state[d][y])):
			if state[d][y][x] == "#" and not (x == 2 and y == 2):
				bugs += 1
print(bugs)