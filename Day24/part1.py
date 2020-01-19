import copy

state = []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		state.append([i for i in line.replace("\n", "")])
		line = f.readline()

prev = []
while not state in prev:
	prev.append([copy.copy(i) for i in state])
	for y in range(len(state)):
		for x in range(len(state[y])):
			adjacent = 0
			adjacent += 1 if x > 0 and prev[-1][y][x-1] == "#" else 0
			adjacent += 1 if x < len(state[y])-1 and prev[-1][y][x+1] == "#" else 0
			adjacent += 1 if y > 0 and prev[-1][y-1][x] == "#" else 0
			adjacent += 1 if y < len(state)-1 and prev[-1][y+1][x] == "#" else 0
			if prev[-1][y][x] == "#" and not adjacent == 1:
				state[y][x] = "."
			elif prev[-1][y][x] == "." and (adjacent == 1 or adjacent == 2):
				state[y][x] = "#"

rating = 0
for i in range(len(state) * len(state[0])):
	rating += (2 ** i) if state[i//len(state)][i%len(state)] == "#" else 0
for i in state:
	print(" ".join(i))
print(rating)